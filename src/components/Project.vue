<template>
    <section class="project">
        <img src="../assets/test/cover.jpeg" alt="cover">
        <div class="info">
            <h1>Enna</h1>
            <h3>28 Août, 2020</h3>
        </div>
        <div class="compteur">
            <button>+</button>
            <span>2</span>
            <button>-</button>
        </div>
    </section>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
$g: 10;
$gap: $g * $g * 0.5;
$height: 15vw;

.project {
  border: none;
  border-radius: 0;
  border-top: 3px solid;
  padding: #{$g}px;
  display: flex;
  align-items: center;
  gap: #{$gap}px;
  width: auto;

  > img {
    border-radius: 10px;
    height: $height;
    width: $height;
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
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
  }
}
</style>