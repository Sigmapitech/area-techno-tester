{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix { system = "x86_64-linux"; };
  in {
    devShells.${pkgs.system}.default = let
      pyenv = pkgs.python3.withPackages (p: [
        p.sqlalchemy
        p.graphviz
      ]);
    in pkgs.mkShell {
      packages = [ pyenv ];
    };
  };
}
