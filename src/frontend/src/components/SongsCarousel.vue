<!-- eslint-disable @typescript-eslint/no-unused-vars -->
<script setup lang="ts">
import { defineProps } from 'vue'
import SongCard from './SongCard.vue';

defineProps<{
  songs: Array<{
    image_url: string;
    song_title: string;
    artist: string;
    album: string;
  }>
}>()
</script>

<template>
  <div class="carousel carousel-center max-w-md p-4 space-x-4 bg-neutral rounded-box">
    <div class="carousel-item w-fit h-fit" v-for="song in songs" :key="song.song_title">
      <SongCard
        :image_url="song.image_url"
        :song_title="song.song_title"
        :artist="song.artist"
        :album="song.album"
      />
    </div>
  </div>
</template>
