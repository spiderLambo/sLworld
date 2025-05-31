<template>
  <Header />
  <main>
    <Artist />
  </main>
</template>

<script setup>
import Header from './components/Header.vue';
import Artist from './components/Artist.vue';
</script>

<style lang="scss" scoped>
main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>