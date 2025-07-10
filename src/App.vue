<template>
  <Header />
  <main>
    <Artist 
    v-for="artist in artists"
    :name="artist.name"
    :profile="artist.profile"
    :projects="artist.projects"
    />
  </main>
  <Footer />
</template>

<script setup>
import Header from './components/Header.vue';
import Artist from './components/Artist.vue';
import Footer from './components/Footer.vue';

const artists = [
  {
    name: "PLK",
    profile: "https://i.scdn.co/image/ab6761610000f1787807ff8b003a33822c40d28c",
    projects: [
      { name: "Enna", cover: "https://i.scdn.co/image/ab67616d00001e02ab779f2adb1007f0321ecab8", date: "2020-08-28", listens: 2 },
      { name: "Polak", cover: "https://i.scdn.co/image/ab67616d00001e029ee288482ec17f1d091ffad2", date: "2021-05-14", listens: 5 },
    ],
  },
  {
    name: "Laylow",
    profile: "https://i.scdn.co/image/ab6761610000f17892f66833fe2a9a854f888042",
    projects: [
      { name: "L'Étrange Histoire de Mr Anderson", cover: "https://i.scdn.co/image/ab67616d00001e029bbbf5ca66b29b25236379cb", date: "2021-10-15", listens: 4 },
    ],
  },
]


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