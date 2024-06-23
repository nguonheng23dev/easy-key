<script setup lang="ts">
import axios from 'axios'
import SearchBar from '../components/SearchBar.vue'
import TitleComponent from '../components/TitleComponent.vue'
import FileInput from '../components/FileInput.vue'
import SongCard from '../components/SongCard.vue'
import SongsCarousel from '../components/SongsCarousel.vue'
import { ref } from 'vue'

const searchResults = ref([])
</script>

<template>
  <main>
    <div class="md:container md:mx-auto text-center mt-8">
      <TitleComponent />
      <SearchBar @search="searchResults = $event" />
      <!-- <FileInput /> -->
      <div class="container">
        <SongsCarousel :songs="searchResults" />
      </div>
    </div>
  </main>
</template>
