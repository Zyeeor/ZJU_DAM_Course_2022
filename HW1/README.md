<h1>#如何实现快速收集歌曲及其专辑封面和歌词</h1>

<h2>#基于开源项目 Musicdownloader <br>
  
  github link: https://github.com/Beadd/MusicDownloader</h2>
 
<h3>#Step 1 选择歌曲</h3><br>
在网易云或QQ音乐中创建想要下载的歌曲歌单，在我的实践中，likes来自于“我喜欢”播放列表，而dislike来自于某个不幸的“抖音热门古风歌曲”（乐）。
<h3>#Step 2 使用Musicdownloader</h3><br>
在正式运行前检查自己的 python3 环境中是否安装了 eyeD3 和 request 库，作为musicdownloader基础的request库如果缺失必须马上安装，eyeD3可以先不必安装（在后续步骤中才会用到）。
<br>
<br>
**TIPS**:eyeD3在downloader项目中用于将歌词及图片嵌入mp3文件中；在我的实践中，由于没有找到mp3中歌词所对应的tags所以使用了比较笨的方法：先不嵌入歌词和专辑封面，将歌词单独下载；然后通过eyeD3嵌入歌词和图片，再将图片单独提取。
<br>
<h3>#Step 3 下载歌曲</h3><br>
运行Musicdownloader.py,跟随软件的指引下载歌单。
<h3>#Step 4 转换歌词格式
运行Musicdownloader.py,跟随软件的指引下载歌单，
运行Musicdownloader.py,跟随软件的指引下载歌单，
