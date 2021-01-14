<template>
<!-- 首页底部 -->
  <div class="bottomIndex">
    <div class="mainBox">
      <el-row :gutter="30">
        <el-col :span="6">
          <h3 class="title">关于北理工</h3>
          <p class="textLi">
            <a href="https://www.bit.edu.cn/">北理工官网</a>
          </p>
          <p class="textLi">
            <a href="https://grd.bit.edu.cn/">北理工研究生院</a>
          </p>
          <p class="textLi">
            <a href="http://lib.bit.edu.cn/">北理工图书馆</a>
          </p>
        </el-col>
         <el-col :span="6">
          <h3 class="title">更多平台</h3>
          <p class="textLi">
            <a href="">兄弟平台1</a>
          </p>
          <p class="textLi">
            <a href="">兄弟平台2</a>
          </p>
          <p class="textLi">
            <a href="">兄弟平台3</a>
          </p>
        </el-col>
        <el-col :span="7">
          <h3 class="title">联系我们 <span class="time">(工作日 9:30-18:30)</span></h3>
          <p class="textLi">
            客服电话：
            <h3 class="number">123456789</h3>
          </p>
          <p class="textLi">
            邮箱：123456789@qq.com
          </p>
          <p class="textLi">
            地址:北京市海淀区中关村南大街5号
          </p>
        </el-col>
        <el-col :span="5">
          <img src="../assets/Main_img/head.jpg" alt="" width="250">
        </el-col>
      </el-row>

    </div>
    <div class="bottomBeian">
      <span>Copyright © 北京理工大学计算机学院 |</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'bottomIndex',
  data() {
    return {
    }
  }
}

</script>

<style scoped>
  .bottomIndex {
    width: 100%;
    height: 330px;
    /* border:1px solid #ddd; */
    margin-top: 1px;
    background: #323232;
  }

  .mainBox {
    width: 1000px;
    height: 280px;
    /* border: 1px solid #ddd; */
    margin: 0 auto;
    text-align : left;
    padding-top:50px;
  }
.title {
    font-size:1.3em;
    color:#fff;

}
.textLi {
    padding:0;
    margin:0;
    line-height: 30px;
    color:#ddd;
}
.time {
    font-size:0.7em;
    color:#999;
}
.number {
    font-size:2em;
    color:#0972d4;
    padding:0;
    margin:0;
}
.textLi a {
    color:#999;
    font-size:0.8em;
    line-height:20px;
}
.bottomBeian {
    background:#000;
    width: 100%;
    height: 30px;
}
.bottomBeian span {
  color: #fff;
  font-size: 0.8em;
  line-height: 30px;
}
</style>
