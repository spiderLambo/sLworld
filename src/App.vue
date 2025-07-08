<template>
  <Header />
  <main>
    <Artist />
    <Artist />
  </main>
  <Footer />
</template>

<script setup>
import Header from './components/Header.vue';
import Artist from './components/Artist.vue';
import Footer from './components/Footer.vue';
</script>

<style lang="scss" scoped>
$gap: 50px;

main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: $gap;
}
</style>