<template>
    <section>
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
$g: 10px;
$gap: $g * ($g / 2px);
$height: 15vw;

section {
  border:none;
  border-radius: 0;
  border-top: 3px solid;
  width: auto;
  padding: $g;
  display: flex;
  align-items: center;
  gap: $gap;

  > img {
    border-radius: 10px;
    height: $height;
    width: $height;
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  }

  .info {
    h1 {
        font-size: $height / 2.5;
    }
    h3 {
        font-size: $height / 9;
    }
  }

  .compteur {
    margin-left: auto;
  }
}
</style>