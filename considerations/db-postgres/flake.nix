{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix { system = "x86_64-linux"; };
  in {
    devShells.${pkgs.system}.default = let
      pyenv = pkgs.python3.withPackages (p: [
        p.graphviz
        p.psycopg2
      ]);
    in pkgs.mkShell {
      packages = with pkgs; [
        graphviz
        pyenv
        feh
      ];
    };
  };
}
