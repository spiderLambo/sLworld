<template>
    <section>
        <header>
            <img src="../assets/test/artist.jpeg" alt="PLK">
            <h6>PLK</h6>
            <div class="menu">
                <img :src="isDark ? listDark : listLight"
                    alt="Passer en mode liste">
                <img :src="isDark ? gridDark : gridLight"
                alt="Passer en mode liste">
            </div>
        </header>
    </section>
</template>

<script setup lang="ts">
import { useTheme } from '../composables/useTheme'
import listLight from '../assets/list-light.svg'
import listDark from '../assets/list-dark.svg'
import gridLight from '../assets/grid-light.svg'
import gridDark from '../assets/grid-dark.svg'


const { isDark, toggleTheme } = useTheme()
</script>

<style scoped lang="scss">
$size: 25px;
$diference: 5px;

section {
    border: 3px solid;
    border-radius: 10px;
    padding: 1rem;
    width: 95vw;
}

header {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    gap: 1vw;
    height: calc($size + 2 * $diference);
    width: 100%;

    > img {
        height: $size;
        border-radius: 50%;
    }

    h6 {
        font-size: $size;
    }

    .menu {
        margin-left: auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 5px;
        border: 1px solid ;
        gap: $diference;
        padding: calc($diference/2);

        img {
            height: calc($size - $diference);
        }
    }
}
</style>