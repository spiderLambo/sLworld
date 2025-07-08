<template>
    <section class="project" :style="{'--height' : props.height + 'vw'}">
        <img :src="props.cover"
         :alt="'Cover de ' + props.name"
         :title="props.name + '\n' + formatDate(props.date)">
        <div class="compteur">
            <button><span>+</span></button>
            <span>{{ props.listen }}</span>
            <button><span>-</span></button>
        </div>
    </section>
</template>

<script setup lang="ts">
const props = defineProps<{
  height: number,
  name: string,
  cover: string,
  date: string,
  listen: number,
}>()

function formatDate(dateStr: string) {
  const date = new Date(dateStr)
  return date.toLocaleDateString('fr-FR', {
    day: '2-digit',
    month: 'long',
    year: 'numeric'
  })
}
</script>

<style scoped lang="scss">
$g: 10;
$gap: $g * 0.1;
$height: 15vw;

.project {
  border: none;
  border-radius: 0;
  padding: calc(#{$g}px * 2);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: #{$gap}vw;
  max-width: 100%;
  width: 100%;
  box-sizing: border-box;

  > img {
    border-radius: 10px;
    height: var(--height);
    width: var(--height);
    box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
    cursor: pointer;

    &:hover {
      transform: scale(1.05);
      transition: transform 0.3s ease-in-out;
    }

  }

  .compteur {
    font-size: calc(var(--height) / 3);
    display: flex;
    justify-content: center;
    align-items: center;
    gap: #{$g}px;

    > button {
      background: none;
      border-radius: 50%;
      border: .5vw solid;
      height: calc(var(--height) / 4);
      width: calc(var(--height) / 4);
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: calc(var(--height) / 4);

      span {
        display: inline-block;
        width: auto;
        padding: 0;
        margin: 0;
        line-height: 1;
        background: none;
      }
    }
  }
}
</style>