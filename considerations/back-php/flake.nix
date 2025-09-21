{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix { system = "x86_64-linux"; };
  in {
    devShells.${pkgs.system}.default = pkgs.mkShell {
      packages = with pkgs; [
        php83
        php83Packages.composer
      ];
    };
  };
}
