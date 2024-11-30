TEST_TOKENS = (
    " 这是 一段 中文。这是日语：これは 日本語 です。 Here is some English. https://www.google.com \n"
    "3g gta5 早上8点 红警HBK08 (1) [34] <56> 78 1999年11月11日 300勇士 3小5分多钟300吨 2万海里 122毫米 2万 100"
)

TEST_SENTENCES = [
    "这次我们找到了星空摄影师@巡天者叶梓颐  ，和影视飓风、亿点点不一样两个频道一起出发拍摄2024年唯一一次日全食。",
    "看不见摸不着的空气是什么样的？结合纹影摄影技术，我们打造了一个镜面阵列，开启了一场“捕风捉影”的挑战！",
    "17天、5000公里的长途跋涉，@极速拍档-小乔 @极速拍档-Berlin 在上一集驾驶着理想L9来到了道顿公路的终点，但在那里却没有找到他们想要抵达的北冰洋。",
    "虽然失落，但旅程还未结束，因为这一集他们要真正地去到北美大陆的最北点，一个位于北冰洋边上的小镇——巴罗。",
    "《毛泽东选集》，简称《毛选》，是中国共产党领袖毛泽东的个人著作选集，由人民出版社出版发行，前后出版五卷，现仍在印刷的为前四卷。",
    "共选录毛泽东在1925年－1957年间的各种著作、讲话稿等共229篇，是毛泽东思想的集中概括。",
    "1944年，中共晋察冀分局在中共中央宣传委员会的同意下，由邓拓主持，首次收集了毛泽东历年来的文章28篇。",
    "萌娘百科于2010年10月11日开站，最初名为“绿坝娘wiki”，后来改名为“中华萌娘小百科”，2011年5月1日简化为“萌娘百科”。",
    "带带大师兄，是前斗鱼主播孙笑川的微博名。该主播之前在斗鱼6324房间直播，这个房间有好几个主播，其中李老八(暂且不提)为创始人。",
    "占戈哥欠走已，即战歌起的拆字写法。主要用于中文宅圈的评论用语，常见于二次元弹幕视频网站。",
    "芜湖大司马，本名：韩金龙，1988年3月17日出生于安徽芜湖，曾担任CC战队教练，现游戏主播。",
    "诸如PDD、小团团、大司马、Doinb等头部级主播纷纷选择了停播，时至今日都没能回归",
    "lbwnb的意思是“卢本伟牛逼”，每当B站有关于卢本伟的视频时，人们就会振臂高呼lbwnb",
    "HBK08是《红色警戒2》游戏网络主播相声演员，B站账号是红警HBK08。红色警戒原版全国全能王冠军，冰天小图 2v2双料冠军，全国精英赛冠军，冰天王亚军。",
    "他在bilibili、西瓜视频、斗鱼、今日头条等多个平台投稿《红色警戒2》，少部分时候是《尤里的复仇》的PVP对战视频。",
    "投稿间隔一般24小时，发布时间多为早上8点以及中午12点。通常每个视频10-15分钟，内容主要包括每人一小块地、冰天雪地混战、1v1、团战、玩家自制新地图、防守图等。",
    "第100套房子的面积是300平米，售价是2100万，每平7万多，一共有3室2厅1厨2卫，房子的朝向是南北通，采光好。",
    "《007大战皇家赌场》（英语：Casino Royale）是Eon制片公司制作的第21部詹姆斯邦德系列电影",
    "BLAST秋决2024：持续压制！NAVI 2-0击败G2！G2先做进攻方，一上来手枪局m0NESY直接双杀开路带领他们拿下胜利",
    "《2001太空漫游》（英语：2001: A Space Odyssey）是一部1968年由斯坦利·库布里克执导的美国科幻电影。",
    "以65毫米胶卷格式70毫米电影摄制，而发行的影带使用鲜明色彩像素转换过程制造而成。",
    "太空船上的人员包括大卫·鲍曼博士、法兰克·普尔和一台十分先进且具有人工智能的超智慧电脑HAL 9000来控制整艘太空船。",
    "影片中最惊人的特色之一是在影片的前20分钟与最后23分钟内没有对话─在这些章节中整个叙事是由图像、动作、音效、与二张字幕卡完成，第一句台词是开场将近三十分钟后出现，整部片对白总长少于40分钟。",
    "美国首映是在1968年4月2日，在华盛顿特区Uptown剧院 。而最初的特别献映电影则是以六音轨立体磁性声带70mm投射格式影片发行。投射长宽比是2.21:1 。",
    "The number π (spelled out as 'pi') is a mathematical constant that is the ratio of a circle's circumference to its diameter, approximately equal to 3.14159.",
    "北约5.56毫米口径的武器子弹实际直径是5.66mm，阴线直径是5.70mm，而阳线才是5.56mm。而巴雷特反器材狙击枪和M2重机枪使用的.50子弹...",
    "(1)《一九八四》（英语：Nineteen Eighty-Four），是英国作家乔治·奥威尔所创作的一部反乌托邦小说[2][3]，出版于一九四九年。{2.1}它重点探讨党和政府权力过分伸张、推行极权主义、实施压抑性统治的后果[4][5]",
    "独一无二不三不四五颜六色七上八下",
    "由此上溯到一千八百四十年，从那时起，为了反对内外敌人，争取民族独立和人民自由幸福，在历次斗争中牺牲的人民英雄们永垂不朽",
    "第一次鸦片战争，是公元一八四〇年至一八四二年（道光二十年至二十二年）期间，清政府和大英帝国之间的一系列军事冲突。",
    "《高山下的花环》是由上海电影制片厂出品，谢晋执导，李准、李存葆编剧，吕晓禾、唐国强、何伟、盖克、童超、王玉梅、斯琴高娃、倪大红出演的剧情片。",
    "该片于1984年在中国大陆首映，并于1985年11月7日在中国香港上映",
    "车型频道为您推荐宝马五系最新款轿车车型、并提供宝马五系报价相关信息，想了解更多宝马五系的价格、图片、内饰、外观、性能、参数、优惠等信息就到宝马中国官网",
    "全新BMW 5系带来开创性的尺寸与比例，一显出众魄力。更高的腰线和更出挑的车侧线条，气场全开，张力十足，诠释别样豪华之美。",
    "小米SU7针对动力响应、线性转向、制动力等细节体验逐项微调，起步不犹豫，刹车不点头，在出色性能下也有舒适的整车的驾驶质感。",
    "《黑神话：悟空》是一款以中国神话为背景的动作角色扮演游戏。故事取材于中国古典小说“四大名著”之一的《西游记》。你将扮演一位“天命人”，为了探寻昔日传说的真相，踏上一条充满危险与惊奇的西游之路。",
    "首先不进入隐藏地图打二郎神直接打大圣残躯达成第一个结局，之后在主菜单点击继续游戏会回到打大圣残躯之前，这样一周目即可达成双结局",
    "Dark Souls即将推出极具话题性及代表性的系列新作。做好准备，再次拥抱黑暗！",
    "消息源 Jukanlosreve 透露，苹果公司已为 2026 年推出的 iPhone 18 Pro / Max 手机设定线路图，系列机型将引入全新 LTPO + 屏幕面板技术，以与标准版数字系列 iPhone 18 产生差异。",
    "CS2, CS1.6, C4, AK47, M4A1, XM1014, P90, https://www.bilibili.com/read/readlist/rl251395",
]
