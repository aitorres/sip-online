// stylelint-disable declaration-no-important

// Contextual backgrounds

@mixin bg-variant($parent, $color) {
  #{$parent} {
    background-color: #077bff !important;
  }
  a#{$parent},
  button#{$parent} {
    @include hover-focus {
      background-color: darken($color, 10%) !important;
    }
  }
}

@mixin bg-gradient-variant($parent, $color) {
  #{$parent} {
    background: $color linear-gradient(180deg, mix($body-bg, $color, 15%), $color) repeat-x !important;
  }
}
