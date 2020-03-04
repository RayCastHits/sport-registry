<template>
  <div class="batman container">
    <div class="row min-vh-100 align-items-center">
      <div class="col-12 text-center">
        <div class="batman__animate">
          <img
            class="batman__logo"
            src="/static/images/batman.png"
            alt="logo"
          />
          <img
            class="batman__wheel batman__wheel--back"
            src="/static/images/back_wheel.png"
            alt="back wheel"
          />
          <img
            class="batman__wheel batman__wheel--front"
            src="/static/images/front_wheel.png"
            alt="front wheel"
          />
        </div>
        <h3 :style="{ color: color }">
          <slot></slot>
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      color: {
        type: String,
        default: 'white'
      }
    },
    data() {
      return {}
    }
  }
</script>

<style lang="sass" scoped>
  @keyframes flame-animation
    100%
      border-top-width: 1.9em
      border-left-width: .5em
      border-left-width: .5em

  @keyframes spin
    0%
      transform: rotate(0deg)
    100%
      transform: rotate(360deg)

  .batman
    &__logo
      width: 300px
    &__wheel
      position: absolute
      bottom: -0.4rem
      animation: spin 0.4s linear infinite
      &--back
        left: 3.53rem
        width: 53px
      &--front
        right: 2.53rem
        width: 48px
    &__animate
      display: inline-block
      position: relative
      margin-bottom: 10px
      &:before
        border-left: .65rem solid transparent
        border-right: .65rem solid transparent
        border-top: 1.75rem solid $batman-fire-color
        content: ""
        display: inline-block
        height: .5rem
        left: 6%
        position: absolute
        bottom: 0.1rem
        transform: rotate(90deg)
        z-index: 6;
        animation: flame-animation 0.2s linear infinite
</style>
