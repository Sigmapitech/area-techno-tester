{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix {
      system = "x86_64-linux";
      config.allowUnfree = true;
    };
  in {
    devShells.${pkgs.system}.default = let
      pyenv = pkgs.python3.withPackages (p: [
        p.pymongo
        p.graphviz
      ]);
    in pkgs.mkShell {
      packages = [
        pyenv
        pkgs.mongodb
      ];
    };
  };
}
