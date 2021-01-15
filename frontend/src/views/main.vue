<template>
  <div id="app">
    <el-row :gutter="20" :style="{background:'url('+logoBackground+')'}" style="padding-top: 10px;">
      <div class="grid-content bg-purple">
        <el-row>
          <el-col :span="24" class="navMain" justify="center">
            <div class="grid-content bg-purple">
              <h1 class="header-h2">POSITIVE——论文检索系统 </h1>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-row>
    <div class="mainwindow">
      <el-carousel height="550px" arrow="always" :interval="3000">
        <div class="bannerSelectInput">
          <el-form :model="ruleForm" :rules="rules" ref="ruleForm" class="ruleForm" :inline="true">
            <el-form-item prop="theme">
              <el-select v-model="ruleForm.theme" multiple placeholder="主题">
                <el-option label="作者" value="author"><span style="float: left">作者</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">Author</span></el-option>
                <el-option label="标题" value="title"><span style="float: left">标题</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">Title</span></el-option>
                <el-option label="摘要" value="abstract"><span style="float: left">摘要</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">Abstract</span></el-option>
              </el-select>
            </el-form-item>
            <el-form-item prop="query">
              <el-autocomplete
                id="search"
                v-model="ruleForm.query"
                :fetch-suggestions="querySearchAsync"
                placeholder="请输入内容"
                @select="handleSelect"
              ></el-autocomplete>
            </el-form-item>
            <el-form-item>
              <el-button class="bor" type="primary" icon="el-icon-search" @click="submitForm('ruleForm')">搜索</el-button>
            </el-form-item>
          </el-form>
        </div>
        <el-carousel-item v-for="(img,index) in imgList" :key="index">
          <img :src="img.url" width="100%" height="100%">
        </el-carousel-item>
      </el-carousel>
    </div>
    <router-view/>
    <bottom-index></bottom-index>

  </div>
</template>


<script>
import {getData} from "@/api/api";
import {getAjaxData} from "@/api/api";
import BottomIndex from '../components/BottomIndex'
export default {
  data() {
    return {
      imgList: [
        {
          url: require('../assets/Main_img/2.jpg')
        },
        {
          url: require('../assets/Main_img/3.jpg')
        },
        {
          url: require('../assets/Main_img/1.jpg')
        },
        {
          url: require('../assets/Main_img/4.jpg')
        }
      ],
      value: '',
      logoBackground: require('../assets/Main_img/indexBanner.jpg'),
      ruleForm: {
        theme: '',
        query: '',
      },
      rules: {
        query: [
          {required: true, message: '不能是空的哦，输入你要查询的内容吧', trigger: 'blur'},
          {min: 0, message: '不能是空的哦，输入你要查询的内容吧', trigger: 'blur'}
        ],
      },
      result: [],
      state: '',
      input: '',
      timeout: null,
      num: 0,
    };
  },
  methods: {
    async Display(params) {
      getData(params)
        .then(res => {
          this.tableData = res.data
        });
    },
    submitForm(ruleForm) {
      this.$refs[ruleForm].validate((valid) => {
        if (valid) {
          this.$router.push({
            name: "Search",
            params: this.ruleForm,
          })
        } else {
          console.log('error submit!!')
          return false;
        }
      });
    },
    querySearchAsync(ruleForm, cb) {
      getAjaxData(this.ruleForm)
        .then(res => {
          this.result = res.data
        });
      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        cb(this.result);                                     //cb()会将json对象的第一个属性拼接到下拉列表中
      }, 3000 * Math.random());
    }, handleSelect(item) {
      console.log(item);
    }
  }
  ,
  components: {
    BottomIndex
  }
  ,
}
;
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.header-h2 {
  font-size: 40px;
  text-shadow: 0px 0px 2px #686868,
  0px 1px 1px #ddd,
  0px 2px 1px #d6d6d6,
  0px 3px 1px #ccc,
  0px 4px 1px #c5c5c5,
  0px 5px 1px #c1c1c1,
  0px 6px 1px #bbb,
  0px 7px 1px #777,
  0px 8px 3px rgba(100, 100, 100, 0.4),
  0px 9px 5px rgba(100, 100, 100, 0.1),
  0px 10px 7px rgba(100, 100, 100, 0.15),
  0px 11px 9px rgba(100, 100, 100, 0.2),
  0px 12px 11px rgba(100, 100, 100, 0.25),
  0px 13px 15px rgba(100, 100, 100, 0.3);
  -webkit-transition: all .1s linear;
  transition: all .1s linear;
  letter-spacing: 25px;
  font-weight: bolder;
}
.header-h2:hover {
  text-shadow: 0px 0px 2px #686868,
  0px 1px 1px #fff,
  0px 2px 1px #fff,
  0px 3px 1px #fff,
  0px 4px 1px #fff,
  0px 5px 1px #fff,
  0px 6px 1px #fff,
  0px 7px 1px #777,
  0px 8px 3px #fff,
  0px 9px 5px #fff,
  0px 10px 7px #fff,
  0px 11px 9px #ffffff,
  0px 12px 11px #fff,
  0px 13px 15px #fff;
  -webkit-transition: all .1s linear;
  transition: all .1s linear;
}
.bannerSelectInput {
  width: 45%;
  height: 70px;
  border: 1px solid rgb(218, 218, 218);
  border-radius: 5px;
  position: relative;
  top: 40%;
  left: 25%;
  z-index: 3;
  /* banner上面的input */
  padding-top: 30px;
  padding-left: 30px;
  background-color: rgba(0, 0, 0, 0.3);
}
.el-select {
  width: 195px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.fontWeight {
  font-weight: 800;
}
.el-row {
  margin-right: 0 !important;
}
.el-input {
  width: 390px;
}
.el-autocomplete{
  width: 390px
}
</style>
