<template lang="pug">
  section(class="section")
    div(class="container")
      div(class="card" v-for="user in users")
        div(class="card-header")
          p(class="card-header-title") {{ user.displayName }}
        div(class="card-content")
          div(class="media")
            div(class="media-left")
              figure(class="image is-256x256")
                img(v-bind:src="user.currentAvatarThumbnailImageUrl")
            div(class="media-content")
              p(class="title is-4") なまえ : {{ user.displayName }}
              p(class="subtitle is-6") すてーたす : {{ user.status }}
              p(class="subtitle is-6") たぐ : {{ user.tags }}
</template>

<script>
  import axios from 'axios'

  export default {
    components: {
    },
    data() {
      return {
        users: null

      }
    },
    mounted() {
      axios.get('http://localhost:8000/api/users/')
        .then(res => (this.users = res.data))
    }

  }
</script>

<style>
  .card {
    margin-bottom: 2em;
  }
</style>

