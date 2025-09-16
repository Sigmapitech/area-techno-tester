{
  description = "Monorepo of area techno tester";

  outputs = { self }:
  let
    pkgs = import ./nixpkgs.nix { system = "x86_64-linux"; };

    collectDevShell = path: name: let
      flake = loadFlake (builtins.toString path + "/${name}/flake.nix");
    in
      { ${name} = (flake.devShells.${pkgs.system}.default or {}); };

    loadFlake = f: (import f).outputs { self = null; };

    listFlakes = f: let
      targets = builtins.attrNames (builtins.readDir f);
    in builtins.map
      (x: collectDevShell f x)
      targets;

    shells = pkgs.lib.lists.foldr (a: b: a // b) {} (
      pkgs.lib.lists.flatten (builtins.map listFlakes [
        ./considerations
        ./pocs
      ])
    );

  in {
    devShells.${pkgs.system} = shells // {
      default = pkgs.mkShell {
        inputsFrom = builtins.attrValues shells;
      };
    };
  };
}
