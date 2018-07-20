1.如何运用svg,注意ie11兼容性问题,下面这个例子不兼容ie11,查看 demo 了解更多.
http://anzhihun.coding.me/ol3-primer/ch07/07-03-03.html

2.styleFunction 应用,styleFunction可以返回单个style,也可以返回array<style>,array<style>的运用方式我没有尝试过.
http://anzhihun.coding.me/ol3-primer/ch07/07-04.html

3.大量图标方案,最主要的是看懂里面提到的 openlayer 例子.
http://anzhihun.coding.me/ol3-primer/ch07/07-05.html
http://openlayers.org/en/v3.17.1/examples/icon-sprite-webgl.html


4.因为ie11存在一些问题所以 svg 文件夹下的所有图标都需要弄成 100px * 100px 大小,以便指定统一的 imgSize ,里面有一部分图标不是 100px * 100px 的需要 UI 调整.

5.文件 svg.py 是一个用 python3 写的爬取gist api的脚本,svg 目录下的 svg 图片就是这样来的.

6.可以把单个 svg 文件合并成一个大的 svg 文件,再利用 offset 和 size 一个一个截取出来,就好像用雪碧图一样, png 图片也可以这样做看下面的例子,合并后的 png 图片就像目录下的 "标志牌styleid.png" 文件,详情可以看 demo .
http://openlayers.org/en/v3.17.1/examples/icon-sprite-webgl.html