let
  ref = "8eaee110344796db060382e15d3af0a9fc396e0e";
in import (fetchTarball {
  url = "https://github.com/NixOS/nixpkgs/archive/${ref}.tar.gz";
  sha256 = "sha256:0vgk8mrprrh6w7zw2id3hc858kqw5pwdc52ma2f95rz36gchxcc4";
})
