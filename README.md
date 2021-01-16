

# 项目内容

- 设计并实现一个学术论文的搜索引擎网站前后端，至少包含这三种页面：首页，搜索结果列表页，论文的详细信息页。可以参考[CrossMinds](https://crossminds.ai/)。
- 首页不仅要有搜索框，还要可以供用户选择要检索的字段（可以同时选择多个字段，比如标题、作者、摘要、全部等等）。用户在搜索框输入文字时，可以实时提示补全信息。（Ajax技术）
- 搜索结果列表页将搜索到的论文按关联度排序展示。
- 论文详细信息页要能播放与论文相关的视频。
- 实现网站架构的前后端分离，数据部分和展示部分分离(MVC)，推荐使用[vue.js](https://cn.vuejs.org/)和[ElementUI](https://element.eleme.cn/#/zh-CN)。
- 推荐使用Python Django（[https://www.djangoproject.com](https://www.djangoproject.com/)）库来实现网站。
- 不需要等检索模块全部完成之后才实现展示模块，和检索模块定义好接口即可进行开发。各模块的开发是并行推进的。
- **模块接口要求**：检索功能通过调用**检索模块提供的Python包**完成，任务开始之前需要和检索模块商量好Python包提供的接口定义。

# 小组成员及分工

| 成员   |    学号    |                            分工                            |
| :----- | :--------: | :--------------------------------------------------------: |
| 刘千会 | 3120201048 | 前后端分离构架搭建、通信实现、前后端逻辑编写、检索模块对接 |
| 余佳奇 | 3220200997 |            所有页面的页面设计及部分对应逻辑实现            |
| 刘琦   | 3120201047 |                 安装文档撰写、部分对接工作                 |
| 张登凯 | 3220201003 |                flake8代码风格测试及对应修改                |
| 李延铭 | 3120201041 |                无（尝试完成：视频传输播放）                |
| 牛泳   | 3220200939 |           无（尝试完成：搜索结果列表页页面设计)            |
| 王红麟 | 3120201067 |                        自动填充功能                        |

# 功能展示

网站主要有三种页面分别为首页，搜索结果列表页，论文的详细信息页，以下为三种页面的图片显示。

![image-20210115171506862](C:\Users\Haley\AppData\Roaming\Typora\typora-user-images\image-20210115171506862.png)

![image-20210115172552554](C:\Users\Haley\AppData\Roaming\Typora\typora-user-images\image-20210115172552554.png)

![image-20210115172149257](C:\Users\Haley\AppData\Roaming\Typora\typora-user-images\image-20210115172149257.png)

网站首页：可以进行带有主题选择的搜索，主题有作者、标题、摘要三种，可以选择零到多个主题，查询带有auto-complete自动填充提示，其中查询不能为空，为空无法进入搜索页面，并且会有相应提示信息。

搜索页面：进入搜索页面，首先显示的是主页的搜索结果，搜索结果分页显示，每次后端只返回一分页大小的数据，当点击下一页或者上一页时，前端会再次向后端发起请求。同时也可以点击表格某一项进入详情页面，此时由于页面跳转，搜素页面的参数将消失，所以在跳转至搜索页面时主题和查询语句这些信息也会传递给搜索页面，当由搜索页面返回时，这些参数信息将再次传递给搜索页面，由此可以向后端发出下一页请求。

详情页面：进入详情页面，如果论文有相应视频，可以自动播放视频，并且显示搜索关键字在视频中出现的时间，页面同时有三个跳转链接，如果论文有相应数据集可以点击下载，论文和源代码可点击新起窗口打开。

同时，VUE设计时设置刷新重新加载，导致页面信息丢失，用户体验感下降，因此在搜索页面和详情页面加入刷新数据保存机制，刷新之前存储数据，刷新过后加载保存数据，防止数据丢失。

# 技术实现及代码结构

本项目采用前后端分离、数据模块和展示模块分离的构架。前端采用VUE+element UI，后端采用Django实现，前端通信采用axios，后端采用rest framework。

## 前端

### 整体结构

#### src-包含所有source  其余文件为创建时自动生成

##### 1.api-封装请求函数 用于前后端数据传输

##### 2.assets-存储UI界面中所用到的图片文件

##### 3.router-路由配置，实现页面切换个拼接

* BottomIndex为主页面和搜索结果页面的底栏设计.vue文件，通过router的方式拼接到对应界面下方。
* Bottominfo为论文详情页面的底栏设计.vue文件，通过router的方式拼接到detail界面下方。

##### 4.utils requiest.js实现前后端互联，封装后端提供的URL

##### 5.views-视图文件，包含所有UI界面具体代码

**UI特色部分介绍：**

* 艺术字设计：ElementUI组件中没有现成的艺术字可以直接使用，在style中设置多种颜色渐变、阴影、倾斜、过渡、悬停变换等特殊效果，美化主题。
* 走马灯展示：通过ElementUI提供的carousel组件实现图片轮播，让界面动态化。在主界面轮播了图片，在detail界面底部轮播了来自<https://cnodejs.org/api/v1/topics>（Node.js专业中文社区)的技术讨论内容。
* 主题选择和远程搜索：用户可以选择相应的主题，输入部分检索信息，从服务端搜索数据以达到填充提示的效果。(用户输入部分目标内容，从服务器端请求数据后提示用户后续内容)
* 视频展示：通过ElementUI提供的video来实现视频自动播放。
* 数据分页展示及溢出悬浮：通过ElementUI提供的组件pagination实现自动分页；添加溢出悬浮来防止信息分栏错乱。

##### 6.components-一些单独设计的组件

##### 7.main.js-全局导入axios、ElementUI、router

### 逻辑介绍

前端视图文件在 src/views文件夹下，分别有main、search、detail三个视图文件构成。

**main.vue** 文件主要视图是有限制的表单，对应名称为ruleForm，用来输入theme和query信息，其中query不能为空，当点击submit按钮时，会触发submitForm函数，这个函数将路由跳转至search界面，同时将theme和query信息一并传递过去。

```
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
```

同时前端用到自动填充功能，使用基于Elementui中的input输入框组件完成，其中的远程搜索组件提供了自动填补搜索框。由于在用户每输入一个字符后，系统就会去请求一次服务器，从而引起抖动问题，通过设置一个初始值为null的timer属性，用户输入一个字符便执行一次clearTimeout(timer)操作，通过timer = setTimeout(() => {"事件"，"时间限定"）来计时，如果两次输入的时间间隔超过时间限定，则进行服务器请求。

```
querySearchAsync(ruleForm, cb) {
      getAjaxData(this.ruleForm)
        .then(res => {
          this.result = res.data
        });
      if (this.result != null) {
        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(this.result);              //cb()会将json对象的第一个属性拼接到下拉列表中
        }, 3000 * Math.random());
      }
    },
    handleSelect(item) {
      console.log(item);
    },
```

**search.vue**文件主要视图由两部分构成，有限制的表单和表格，分别用来输入查询信息，展示搜索结果信息。当路由跳转后，依次触发created和mounted函数，search页面首先接收main传来的搜索参数，并将其存储到state状态中，并将分页page设为1，同时向后端发出请求。如果页面刷新，search页面将从state中加载状态信息，防止页面丢失。

```
  mounted() {
    this.params = this.$route.params
    if (this.params.query !== undefined) {
      this.$store.commit('saveParams', this.params)
      this.handleCurrentChange(1)
    } else {
      this.params = this.$store.getters.myParams
      this.handleCurrentChange(this.$store.getters.myCurrentPage)
    }
  },
```

信息的存储加载主要是通过store文件夹中的index.js实现的，用来存储三个状态，search页面的query和theme信息，以及detail页面的所有信息。每次search界面搜索时会更新存储的搜索参数，每次点击点击下一页时，也会更新存储的页码参数。并用createPersistedState这个插件实现刷新的持久化。

```
const store = new Vuex.Store({
  state: {
    detail: null,
    currentPage: null,
    params: null

  },
  mutations: {
    saveDetail(state, detail) {
      state.detail = detail
    },
    saveCurrentPage(state, params) {
      state.currentPage = params
    },
    saveParams(state, params) {
      state.params = params
    }
  },
  getters: {
    myDetail(state) {
      return state.detail
    },
    myCurrentPage(state) {
      return state.currentPage
    },
    myParams(state) {
      return state.params
    }
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState()],

})
```

handleCurrentChange函数用来实现页码改变，同时调用Display函数向后端发送请求，display函数调用封装好的axios接口，实现向后端进行数据传输，并将返回的结果赋值为展示搜索结果的table。

```
handleCurrentChange(val) {
	this.currentPage = val
    this.params.page = this.currentPage
    this.Display(this.params)
    this.saveCurrentPage(this.currentPage)
}
Display(params) {
	getData(params)
        .then(res => {
          this.tableData = res.data.data
          this.totalCount = res.data.total
        });
   	}   
```

当用户点击table中的某一行时，将触发openDetail函数，将这一行的信息封装，并路由至detail页面，由detail页面展示这些信息。

```
openDetail(row) {
      if (row) {
        this.$router.push({
          name: 'Detail',
          params: {
            video: row.video,
            title: row.title,
            abstract: row.abstract,
            dataset_url: row.dataset_url,
            keyword_in_video_time: row.keyword_in_video_time,
            pdf: row.pdf,
            author: row.author,
            publish_at: row.publish_at,
            publisher: row.publisher,
            params: this.params
          }
        })
    }
```

**detail.vue**主要展示detail信息，在路由跳转后，也是依次触发created和mounted函数，和search页面一样，首先判断是路由跳转还是刷新，如果是路由，则存储相应参数并展示，如果是刷新，则加载store中的state。

```
created() {
    let params = this.$route.params
    if (params.title !== undefined) {
      this.$store.commit('saveDetail', params)
    } else {
      params = this.$store.getters.myDetail
    }
```

下面是前后端通信接口，在/utils/requiest.js文件中使用自定义配置新建一个 axios 实例，/api/api.js中用于管理请求。getData用来获取搜索结果，getAjaxData用来获取自动填充结果。

```
const axiosInstance = axios.create(
  {
    baseURL: 'http://localhost:8090/polls',
    timeout: 1000
  }
);

export const getData = (param) => {
  return requiest(
    {
      url: "/query",
      method: 'get',
      params: param
    }
  )
}
export const getAjaxData = (param) => {
  return requiest(
    {
      url: "/hint",
      method: 'get',
      params: param
    }
  )
}
```

## 后端

项目初期，为了项目顺利推进，我们在本地自建了数据库，通过精确搜索测试并完成相应通讯，代码使用了view的第五级视图ModelViewSet，自建的序列化功能，以及模型映射现已无用。

### 整体结构

#### 1.backend文件夹主要用到setting.py进行相关信息配置，urls.py进行路由转发。

#### 2.polls文件夹主要用到urls.py进行连接到方法的映射，views.py用于相关请求的实现。

### 逻辑实现

对于前端发送的请求先由urls.py文件进行转发，由于网址是http://localhost:8090/polls，所以转发至polls文件夹的urls.py。

```
router = routers.DefaultRouter()
router.register('polls', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    # path('polls/', include('polls.urls'))
]
```

polls/urls/接收后，根据前端传输的网址，分别调用不同方法，如：/query和/hint分别调用polls/views.py下的query和hint方法。query将解析url一同传递过来的参数query，theme（可能为空），page，并将这三个参数传递给检索模块，返回结果，通过rest framework中的Response方法返回给前端，hint同理。

```
 @action(detail=False, methods=['get'])
    def query(self, request):
        theme = self.request.query_params.getlist('theme[]', None)
        theme = ','.join(theme)
        query = self.request.query_params.get('query', None)
        page = self.request.query_params.get('page', None)
        data = search(query, theme=theme, page=page)
        return Response(data)

    @action(detail=False, methods=['get'])
    def hint(self, request):
        query = self.request.query_params.get('query', None)
        data = get_suggestion(query)
        return Response(data)
```



#  部署过程及启动流程

## 前端

### 安装node.js

###### Node.js 安装包及源码下载地址为：<https://nodejs.org/en/download/>

### project setup 安装依赖

```
npm install
```

#### 安装ElementUI

```
npm i element-ui -S
```

```
# 推荐使用 npm 的方式安装，它能更好地和 webpack 打包工具配合使用。
```

#### compiles and hot-reloads for development 运行程序

```
npm serve
```

#### bulid for production with minification 打包

```
npm run build
```

### 安装axios

```
npm install axios --save
```

### 安装persistedstate

```
npm install --save vuex-persistedstate
```

### 启动命令

```
npm run serve
```

## 后端

### 安装命令

```
pip install -r requirements.txt
```

### 启动命令

```
net start MongoDB
python manage.py runserver 8090
```

