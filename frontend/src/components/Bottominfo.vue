<template>
  <el-carousel trigger="click" height="150px"  :style="{background: 'url('+bottomBg+')'}">
    <el-carousel-item v-for="item in tableData" :key="item.text" class="bannerText">
      <h3>{{ item.title }}</h3>
      <!-- <img src="pic/{{ item }}.jpg" alt=""> -->
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  name: 'Bottominfo',
  data() {
    return {
      tableData: '',
      bottomBg : require('../assets/Main_img/2.jpg')
      // bannersearchbtn : ''
    }
  },
  created() {
    this.$http.get('https://cnodejs.org/api/v1/topics', {
      params: {
        page: 1,
        limit: 5
      }
    }).then(res => {
      this.tableData = res.data.data;
      console.log(this.tableData[0].create_at);
    }, response => {
      console.log("res");
    })
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 2em;
  opacity: 0.75;
  line-height: 50px;
  margin: 0;
}
</style>
