{
  outputs = { self }: let
    pkgs = import ../../nixpkgs.nix {
      system = "x86_64-linux";
      config = {
        allowUnfree = true;
        android_sdk.accept_license = true;
      };
    };
  in {
    devShells.${pkgs.system}.default = pkgs.mkShell {
      packages = with pkgs; [
        nodejs
        jdk
        androidenv.androidPkgs.androidsdk
      ];
    };
  };
}
