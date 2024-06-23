<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { defineProps, defineEmits } from 'vue'
import { flushPromises } from '@vue/test-utils'

const emit = defineEmits(['search'])

const searchBarText = ref('')
const response = ref([])

const submit = async () => {
  try {
    const { data } = await axios.get(`http://localhost:8000/search?query=${searchBarText.value}`)
    const tracks = data.tracks.items.map((track: any) => ({
      id: track.id,
      song_title: track.name,
      artist: track.artists[0].name,
      album: track.album.name,
      image_url: track.album.images[0].url,
      playback: track.preview_url
    }))
    emit('search', tracks)
    flushPromises()
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
  <div class="md:container md:mx-auto px-3">
    <input
      type="text"
      v-model.lazy="searchBarText"
      placeholder="Houdini - Dua Lipa"
      class="input input-bordered input-secondary input-lg w-full max-w-xs mr-2"
    />
    <button v-on:click="submit()" class="btn btn-secondary btn-lg">Search</button>
  </div>
</template>
