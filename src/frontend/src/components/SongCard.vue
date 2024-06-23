<script setup lang="ts">
import { defineProps } from 'vue'

// Define the props with TypeScript
defineProps<{
  image_url: string;
  song_title: string;
  artist: string;
  album: string;
}>()
</script>

<template>
  <div class="card bg-base-100 shadow-xl">
    <figure class="relative">
      <img :src="image_url" :alt="`Album photo - ${album}`" />
      <button class="btn btn-circle btn-lg absolute z-10">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="icon icon-tabler icon-tabler-play"
          width="44"
          height="44"
          viewBox="0 0 20 24"
          stroke-width="1"
          stroke="currentColor"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <path d="M5 3l14 9l-14 9z" />
        </svg>
      </button>
    </figure>
    <div class="card-body">
      <h2 class="card-title">
        {{ song_title }}
        <div class="badge badge-secondary">NEW</div>
      </h2>
      <p>Artist: {{ artist }}</p>
      <p>Album: {{ album }}</p>
      <div class="card-actions justify-end">
        <div class="badge badge-outline">Previous</div>
        <div class="badge badge-outline">Next</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
p {
  text-align: left;
}
</style>
