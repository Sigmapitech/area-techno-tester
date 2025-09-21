{
   outputs = _: let
     pkgs = import ../../nixpkgs.nix {
       system = "x86_64-linux";
       config.allowUnfree = true;
       config.android_sdk.accept_license = true;
     };
   in {
    devShells.${pkgs.system}.default = pkgs.mkShell { };
   };
}
