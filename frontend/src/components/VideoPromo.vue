<template>
 <div  class="container__video">
   <div class="preview__wrap">
     <router-link :to="'/video/' + video.video_id">
       <img :src="pre" class="preview" alt="Видео">
     </router-link>
       <div class="v">
           <router-link :to="'/video/' + video.video_id" style="text-decoration: none; color: inherit;">
               <a class="name">
                   {{ video.name }}
               </a>
           </router-link>
           <router-link :to="'/account/' + video.user_id" class="username">
               Автор: {{ video.username }}
           </router-link>
           <p class="username">Просмотры: {{ video.count_views }}</p></div>
   </div>
 </div>
</template>

<script>
export default {
  name: "video-promo",
  props: {
    video: { type: Object, required: true }
  },
  data() {
    return {
      pre: require('../assets/video/default_preview.jpeg')
    }
  },
  mounted() {
      if (this.video.preview_url) {
          this.pre = this.video.preview_url;
      }

  }
}
</script>

<style scoped>
.v {
    padding-left: 15px;
}
.container__video {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 0;
  gap: 19px;
  margin-bottom: 20px;

  width: 33%;
  height: 293px;
}
.preview__wrap {
  width: 344px;
  height: 200px;
  background-color: var(--background-color);
  border-radius: 10px;
}
.preview {
    margin-bottom: 20px;
    border-radius: 10px;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.name {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 18px;
  text-transform: uppercase;
  text-align: inherit;
  margin-bottom: 0;
}
.username {
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 18px;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-decoration: none;
  border-bottom: 0;
}
.username, .name, .username:hover, .name:hover, .name:active, .name:focus {
  color: var(--color-text);
  text-decoration: none;
}
</style>