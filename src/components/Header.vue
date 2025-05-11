<template>
    <header>
        <nav>
            <ul>
                <li><img src="../assets/pp.webp" alt="Nom d'utilisateur" class="pp"></li>
                <li><img src="../../public/sLmusic-big.svg" alt="🎵 sLmusic"></li>
            </ul>
            <ul>
                <li>Ajouter</li>
                <li><img src="../assets/moon-line.svg" alt="Mode nuit"></li>
            </ul>
        </nav>
    </header>
</template>

<style lang="scss" scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 75px;
  padding: 0 2rem;

  ul {
    display: flex;
    gap: 20px;
    align-items: center;
  }

  li {
      list-style-type: none;
      
      img {
          height: 24px;
      }
  }
}

.pp{
    height: 40px;
    border-radius: 50%;
}
</style>

<script setup></script>