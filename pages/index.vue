<template>
  <div>
    <section class="mb-5">
      <v-parallax style="background-color : grey;" height="300">
        <v-layout column align-center justify-center class="white--text">
          <h1 class="white--text mb-2 display-1 text-center">
            <b>{{$t("honchoseiki")}}
            </b>
          </h1>
          <v-btn
            large
            class="mt-5"
            :to="localePath({ name: 'list' })"
            color="primary"
            >{{ $t('try_out') }}</v-btn
          >
        </v-layout>
      </v-parallax>
    </section>

    <v-container>
      <v-card class="my-5">
        <v-card-title>
          <h2>{{ $t('about_') }}</h2>
        </v-card-title>
        <v-card-text>
          <div class="text--primary">
            <p>{{$t("honchoseiki")}}</p>
          </div>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      baseUrl: process.env.BASE_URL,
    }
  },
  head() {
    const title = this.$t("hochoseiki")
    return {
      titleTemplate: null,
      title,
    }
  },
}
</script>
