<template>
  <div id="app" class="container">
    <v-toolbar
      dark
      prominent
      
    >
      <v-toolbar-title centered>Movie Cave</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-tabs
      fixed-tabs
      centered
      dark
    >
      <v-tab to="/">Home</v-tab>
      <v-tab to="/login">Login</v-tab>
      <v-tab to="/profile">Profile</v-tab>
      <v-tab to="/worldcup">World Cup</v-tab>
    </v-tabs>
    <div class="row justify-content-center">
      <router-view class="col-12"/>
    </div>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}

</style>
