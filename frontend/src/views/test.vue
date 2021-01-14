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
    <el-container class="Detail">
      <!--      <div class="Detail">-->
      <el-aside width="640px">
        <div class="video">
          <video width="640" height="480" controls autoplay>
            <source :src="video" type="video/mp4">
          </video>
          <div class="videotime">
            输入的关键字位于视频：{{ keyword_in_video_time }}
          </div>
        </div>
      </el-aside>
      <el-main>
        <el-container class="maininfo">
          <el-header>
            <el-row>
              <el-col :span="8">
                <h2 class="titlehot">{{ title }}
                </h2>
              </el-col>
              <el-col :offset="14" :span="2">
                <el-button icon="el-icon-back" @click="back" plain>返回</el-button>
              </el-col>
            </el-row>
          </el-header>
          <el-main>
            <h5>
              {{ author }}
            </h5>
            <div class="article">
              <div>
                摘要：{{ abstract }}
              </div>
              <br><br>
              <div>
                出版社：{{ publisher }}
              </div>
              <br>
              <div>
                出版年份：{{ publish_at }}
              </div>
            </div>
            <div class="indexbox">
              <div class="boxFour"
              <el-row :gutter="10" justify="center">
                <el-col :span="8">
                  <a :href="this.pdf" target="_blank" style="color: white">
                    <i class="el-icon-document"></i>
                    <h3>论文原文</h3>
                    <h5>PDF</h5>
                  </a>
                </el-col>
                <el-col :span="8">
                  <a :href="this.dataset_url" target="_blank" style="color: white">
                    <i class="el-icon-document"></i>
                    <h3>数据集</h3>
                    <h5>Dataset</h5>
                  </a>
                </el-col>
                <el-col :span="8">
                  <a :href="this.pdf" target="_blank" style="color: white">
                    <i class="el-icon-document"></i>
                    <h3>源代码</h3>
                    <h5>Code</h5>
                  </a>
                </el-col>
              </el-row>
            </div>
          </el-main>
        </el-container>
      </el-main>
    </el-container>
    <bottominfo></bottominfo>
  </div>
</template>

<script>
import Bottominfo from '@/components/Bottominfo'

export default {
  data() {
    return {
      logoBackground: require('../assets/Main_img/indexBanner.jpg'),
      video: [],
      vforitem: [{
        name: "论文原文",
        english: "PDF",
        icon: "el-icon-document",
        url: "https://www.csdn.net/"
      },
        {
          name: "数据集",
          english: "Dataset",
          icon: "el-icon-s-grid",
          url: []
        },
        {
          name: "源代码",
          english: "Code",
          icon: "el-icon-edit-outline",
          url: []
        }
      ]
    }
  }, created() {
    let params = this.$route.params
    if (params.video !== undefined) {
      this.$store.commit('saveDetail', params)
    } else {
      params = this.$store.getters.myDetail
    }
    this.video = params.video
    this.title = params.tittle
    this.dataset_url = params.dataset_url
    this.abstract = params.abstract
    this.keyword_in_video_time = params.keyword_in_video_time
    this.pdf = params.pdf
    this.publisher = params.publisher
    this.publish_at = params.publish_at
    this.author = params.author
  }, components: {
    Bottominfo
  },
  methods: {
    async Display(params) {
      getVideo(params)
        .then(res => {
          this.video = res.data
        });
    },
    back() {
      this.$router.push({name: 'Search'})
    }
  },
}
</script>

<style lang="less" scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
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

.Detail {
  background: url("../assets/img/hotback.png");
  height: 750px;
}

.video {
  text-align: center;
}

.btn {
  text-align: center;

  button {
    width: 15%;
    margin: 0 10px;
  }
}

.indexbox {
  test-align: center;
  padding-top: 180px;
  padding-bottom: 0px;
}

.boxFour {
  line-height: 10px;
  margin: 0;
  -webkit-margin-before: 0em;
  -webkit-margin-after: 0em;
  -webkit-margin-start: 220px;
  -webkit-margin-end: 0px;
  padding-top: 80px;
  /* border:1px solid #ddd; */
}

.boxFour:hover a {
  color: #01050a;
}

.boxFour .look {
  color: white;
  font-size: 0.8em;
}

a {
  text-decoration: none;
}

.titlehot {
  padding-top: 0%;
  width: 1000px;
  color: #fff;
  font-family: "黑体";
  padding-bottom: 2%;
  font-size: 2em;
  letter-spacing: 10px;
  font-weight: 800;
  padding-left: 0px;
}

.maininfo {
  color: white;
}

.article {
  text-align: left;
}

.videotime {
  color: white;
}

.el-button--danger.is-disabled:hover {
  background-color: #eee;
  border: 1px solid #ccc;
}
</style>
