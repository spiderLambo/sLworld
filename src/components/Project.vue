<template>
    <section class="project">
        <img src="../assets/test/cover.jpeg" alt="Cover de Enna" title="Enna">
        <div class="info">
            <h1>Enna</h1>
            <h3>28 Août, 2020</h3>
        </div>
        <div class="compteur">
            <button><span>+</span></button>
            <span>2</span>
            <button><span>-</span></button>
        </div>
    </section>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
$g: 10;
$gap: $g * 0.4;
$height: 15vw;

.project {
  border: none;
  border-radius: 0;
  border-top: 3px solid;
  padding: calc(#{$g}px * 2);
  display: flex;
  align-items: center;
  gap: #{$gap}vw;
  width: auto;

  > img {
    border-radius: 10px;
    height: calc(#{$height});
    width: calc(#{$height});
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

    &:hover {
      transform: scale(1.05);
      transition: transform 0.3s ease-in-out;
    }

  }

  .info {
    h1 {
        font-size: calc($height / 2.5);
    }
    h3 {
        font-size: calc($height / 9);
    }
  }

  .compteur {
    margin-left: auto;
    font-size: calc($height / 3);
    display: flex;
    align-items: center;
    gap: #{$g}px;

    > button {
      background: none;
      border-radius: 50%;
      border: .5vw solid;
      height: calc($height / 4);
      width: calc($height / 4);
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: calc($height / 4);

      span {
        display: inline-block;
        width: auto;
        padding: 0;
        margin: 0;
        line-height: 1;
        background: none;
      }

      // &:first-child span {
      //   transform: translateY(-1px);
      // }

      // &:last-child span {
      //   transform: translateY(-3px);
      // }
    }
  }
}
</style>