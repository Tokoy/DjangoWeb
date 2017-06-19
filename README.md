# DjangoWeb
PreView：
![网站预览](https://github.com/Tokoy/DjangoWeb/raw/master/common_static/img/PreView.png)  

以该项目为例子简单介绍下，该网站用Python的Django和angularjs 外加bootstarp生成的   
Django：用来作为后台管理（数据的存储和调用，管理之类的）  
Angularjs：后台传来的数据将会以URL的形式来传递数据，数据的类型为json格式，这种传递的方式称为REST。  
bootstrap：一个很好的针对前段页面美观的框架，可增加页面的美观和便捷。   
现在来分析下各个文件夹下的文件的作用：  
HelloDjango文件夹  
-init.py:   一个空文件，告诉Python 该目录是一个 Python 包。  
-serializers.py ：主要用来定义ViewSet，从后台数据库那获取数据，然后定义页面上可以显示的数据有哪些，这些称为Serializer。  
-settings.py：该 Django 项目的设置/配置，如果有添加一些apps，都需要到里面定义好，静态资源的地址也是这里设置好。  
-urls.py ：主要用来定义各种URL，Django里是类似于调用方法，把一些url设置为方法，使用直接调用url就可以了，一份由 Django 驱动的网站"目录"。  
-wsgi.py ：一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。  
此文件夹里都是Django自动生成的文件。  
TESTWEB：该文件夹主要是前台页面代码，所有前台页面相关的代码都在这里。  
Collected_static:STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来。  
Common_static:其它存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT。  
hello文件夹  
-migrations  :migrations机制有两个指令，第一个是makemigrations，第二个是migrate，生成migrations代码的makemigrations指令是用models里面的。model和当前的migrations代码里面的model做对比，如果有新的修改，就生成新的migrations代码。所以该文件夹里的文件是models里定义好数据表后使用命令生成出来的，如果需要对数据表进行修改，这更改models里的数据后再重新生成一遍。  
-init.py:告诉Python这也是一个Python包。  
-admin:主要用来注册models的，如果需要定义一个新的models也需要在这里定义好。  
-apps.py:暂时还没怎么用到，是用来对一些apps进行命名。  
-models.py :创建数据表结构。  
-views.py:用来定义一些方法，可以在url里去调用这些方法。  
manage.py:一个Django的命令行工具，调用这个文件用里面的一些命令可以很方便的与django项目进行操作。   

文件的介绍大致就是这些，主要思路还是前台后后台尽量分离，前台页面主要进行数据的显示，这点angularjs很好的可以进行及时的显示，只要数据有变动，页面上就可以直接显示无需刷新页面，bootstarp主要是显示页面上的美观，具体数据的显示操作用angularjs可以直接操作，这些都属于前台的东西。
后台的话主要由Python的Django来全部控制，数据进行一些操作，定义方法，建立数据库，管理数据，以URL的形式向前台页面进行数据传递，这边完全是后台相关的操作，与前台页面分离。
前台与后台之间只是单纯的数据交换，没有其他交际，数据的交换就可以直接用Angularjs 的$http（POST和GET），对地址进行一些CRUD。

关于该网站的一些构思，本来只是个人兴趣想学一学Python语言，之前也刚好做了一些angularjs 的项目，就想能不能两个结合起来制作一个Python+Angularjs 的网站或者是个人博客，慢慢的了解学习后发现确实可行，Django作为Python里面一款基于MVC构造的Web框架 ，应用也非常广泛，比较有名的instagram（2亿用户量）也是由Django写出来的，所以完全可以用来写一个轻量级的个人博客网站，网站的功能主要是用来显示自己写的一些博文，新闻之类的，普通的浏览器用户也可以对文章发表一些评论，投票，点赞之类的，最好能针对用户自动显示管理员界面或者是普通用户界面，管理员界面可以点击发表文章，普通用户则没有，暂时先这些功能，页面尽量简洁美观，这样也利于移动端的显示，angularjs本身也有对移动端的进行优化，暂时介绍就写到这里，虽然只是个人兴趣，但还是希望可以利于自己慢慢完善这个项目。

完整的框架就是这样，想要写好一个完整的版本，需要对angularjs，bootstarp，Python(Django)的基础知识具有一定的了解，Python的功能很强大，bootstarp的页面也很美观，angularjs作为其中前台与后台的交互语言也很出色，想要写好网站可以参考一些相关的实例，国外也有专门的Angular-Django的实例网站，里面有许多很有用的轮子可以用。
