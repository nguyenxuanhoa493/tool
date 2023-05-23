import sys
sys.path.insert(0, '/Users/mamang/Library/CloudStorage/OneDrive-Personal/Tools/API')
sys.path.insert(0, r'C:\Users\nguye\OneDrive\Tools\API')

import info
import contest

list_take = """64338a87e290a40ad331f6a5
64339be293fb3879cf51207f
64339ddcee9fe43ab4294bbc
64339fbdf03dbe60a70b6484
6433bf84695b65338f3f9a04
64340a2ffab3fb09eb5e7d71
64340e59d835911d566367cb
64340eead693425a704fdf48
643410904d2009659727a172
6434115cd77dcc33313fdba0
64352f8c6f8c5c3fda407339
64353011c656f87a4c363708
6433a4df96bcb64c307aa88c
64353cb557abc30c644972fc
64353cff07d51d301a1219c6
6435401b34ccce7a1c4601ec
64354927482aa8552532338f
64354cca3ac1f25b6f288b82
64356b6ddece923db94bbf50
643575c5c2817e5c7a0a6459
64340add99bdd639be241329
6435f7d9ea0aa217f3667fbf
6435f893886041356d5243ca
64339d9949401714c574ba25
6435fa224f50ec20ec6f81ca
6435faabad851257db773fbf
6435fbcb6d715b29d851fde1
6435fc3a38da3769320d10de
6436253fb4e5d23af22aa0c8
6436485094f38a3e7d7a0420
64364bbdbf5d88793b1095ab
64364c7dd906877b5308f3f7
64364d0b1bb4b1634d0ab393
64364d8f0d2ce620d026bfed
64364e115c1895003c20bfd1
6436559d9a691f6afa2bbdd1
643656067dcba502215b43e9
64366fc02cb72e63d37cb9b6
6436708d5d894d68ae36a8e1
643682fca93e8907b805ef83
643683a66d0c6e552357afae
643684531b3bb26ca67a4ece
643688a5ee2dac640f75c002
643688eecd98a3076963a1e5
6436893bd823a23d954f8e8a
643689b53a10ce3d303520ba
64368a00cf5d3b59f47316b7
64368aa8bc10a9053a734e50
64368b499a691f6afa2bc069
64368b759906a27d0359561b
64368ba5dd46de1f487fdf04
64368c1d1f677a11640b777e
64368c6994e7fb0dc004292c
64368cd4187a6263fc56ca8c
64368d237928fc321f6ef10a
64368d7ed41f4c5af8608968
64368dad5fdca656343005f1
64368ddd3315756b1e226f2c
64368e0b8d74080b465e8785
64369187f9cb386c931a648b
6436926129f7dd65b0559624
643692df791470590e2c6dd2
6436937d70e063225c461002
643693ee993398689f598dea
6436945e1e139d49a2228f3f
64369b4d6ee56b74d06f5c24
64369caa38d8fc5bea17e3ac
64369f0c3a10ce3d303521ba
64356cd4499d437a0758a9c2
6436b074c53c7552135a19dc
6436b1814f50ec20ec6f8944
6436b42eaa00f10af6420414
6436b646d41f4c5af8608b37
6436b773879f197ed13a3ffd
6436b8131e8b2578dc3b8fd8
6436b913ed3f8f3f72662f44
6436ba31aa6e2b03f32634c6
6436bae64b47ab531a17c661
6436bb3915ded0033f317915
6436bb88dfb039512d01d164
6436bd426d0c6e552357b215
6436bd7fcd250a2dfe5cfe90
6436bda5cb19b10313440482
6436be6c7643f50dde468bb9
6436bea1cbf62b4e7e2b3d06
6436bf0eda72860e27673829
6436bf3eb4ac6b56e71350ff
6436bf6af145d065a5318a32
6436bfab1db6a612523a965a
6436c082a6de450de05e22fd
6436c0cf9405a172eb11ea85
6436c1cf05d71074bb2ca6e8
6436c239cb46616f80798a4d
6436c25d15ded0033f317967
6436c29d4da1111a8a42c275
6436c7bc1a47fe0b9f4eb1ee
6436d0f7ae5dc17e62045c02
6436d13a2d93242f466c7b5c
6436d17c3fd5c66bfa7a9d73
6436a4ee5327a14c06107799
6436d9f8eca8dd510d613e21
6436dc88cb8a75585e28bd0d
6436dd2076f93d2b1115a657
6436ddb07094ea1a1a2ce1d2
6436de478a1ad52d7965c826
6436dedf7643f50dde468d19
6436df42e712a755442ae7b8
6436dfaa06ccb71c002d5d80
6436e00135e27c42e2512d86
6436e0583c041573792136ac
6436e0c0cd722d0679368415
6436e1011db6a612523a97de
6436e15409f4ba604c6dda77
6436e1e0ae88b039914970f1
6436e28a35b09b47250fe8c7
6436e2e191be13318e74c745
6436e33a3e1cf75fe8543210
6436e3da3e1cf75fe8543219
6436e42e02cb026a5e32ff5f
6436e4790c42fe4e767009e8
6436e4cf4c9e636795021578
6436e595288a1a0e0219910a
643694c7b75e8f49ba178246
64353f158e7104222e47d048
6436331c3519a260581edfdb
643779e0b1b2e12917287741
64377ab9dfb039512d01d62e
64378e23ad851257db774d64
64378f5d81cde8228d5807fc
64378fa5f53c845e775d7ac1
64378fc40ab568124f699a1e
6437a50a4b0b9f03cd6b61c4
6437a5bec1cb1a7fcd06ab8d
6437a663218b6372a9294db9
6437ada0b47f8a5be6564c5d
6437af6d798ece1fbb483980
6437b0c08e67f561951abc60
6437b1b1d53007030f2e63c8
6436e9ca5540704c3436bb73
6437cc27d39ea11d9d0c3490
6437cc723eed0d6ad26bbe38
6437cc005b72c117c019448e
6437ccb4b0cbac798966ed7d
6437cd016e19f232f44249f0
6437cd42b8d2184e35389df4
6437cd781b3bb26ca67a5a4f
6437cdb4cd98a3076963ad8d
6437cdea1efff57f5539f3aa
6437cd87a3c4cd5f6e70df18
6437ce27175a093807302b1b
6437d6d6a29ab2408b7208cd
6437d70abc10a9053a7359ac
6437d7424b47ab531a17cfbb
6437d77bdf19396d240527e1
6437d8071b3bb26ca67a5ab6
6437d83b1a59801fb52d957c
6437d88cc1ec04354a42193b
6437ded635e27c42e2513553
6437dfeff649300d9054dd52
6437e0d6e0d32d2d7c1a3248
6437e18b9235f42fe45e2047
6437e2436e3a9e474a1f64f6
6437e3153b2f98072741a809
6437e3d2e7b90e105a0fd680
6437e48abd06721c7848c19a
6437e5045540704c3436c373
64378c740e8c52416e74c9e9
6437ebfbc5e38f407e6a20cd
6437f5af82b2c53ca76e7b25
6437f61a288a1a0e021999ac
6437f67b3b0d8914fd06c32c
6437f6ce20836937c105f079
6437f71d35b09b47250ff209
6437f89efcf39344a756b38a
6437fe1bee218913fa46e8cf
6437fe61249b8c0c6a4fd130
64380f5f39a5f6540667551b
64380fdb78065b19d50c732f
643787f9fe76364dc55d4c07
64381945f62343747534a894
6437d8bebcf8d02c58732ee3
64381bd6524ed542f039ebd6
64382179d906877b5309061d
643821f805adfb391901230e
6438226d57eab31fde2446b8
6438231d90527b71f75267eb
643823d8879f197ed13a4da0
6438247b6e2d05538361138a
643824d6f0e5105c63315381
64382540218b6372a9295471
643825d9ff150a180909534a
64382679057cd36a6b6ff59c
6438c032cd250a2dfe5d0f76
6438c242187a6263fc56dd19
6438ca6a6e19f232f44252ba
6437ed8aab727a49d61c884f
64393745f6f4523cab56eea1
643a196520ffb04dff668bbe
643a77dceca8dd510d61590c
6435fb48401369542a6210ac
643b8237c5e38f407e6a39c8
643b8430516b6819fa0c5d1c
643b880efe76364dc55d687b
643b88fedc8aac61d66540e2
643938cbbf5d88793b10af3d
643c0a2212bf6b245672a78a
643c0b86bf5d88793b10bfc6
643c0cf9062f74560d701e40
643c0de5291e514a9d74a68b
643c0fb54b0b9f03cd6b816c
643c10b677e30919f91e8de7
643c1326572b9a5cc530a75c
643c140f7150364c2c653e6d
643c13e1fe1dc600433e62ce
643c14a62683a528824640af
643c14ef47e75e128e448537
643c15b07094ea1a1a2d05fb
643c16825d894d68ae36d27a
643c173517484f03696614d1
643c18130e81f778e2652989
643c18f4c7b70c2c1445a3bb
643c19ed0420de61f8051a6b
643c1aeda990b54fc20eaf9e
643c1bbff542365bcb46a02e
643c1cdff2e1a3390c02be72
643c86b989318f63435c9d8a
643c87b20ab568124f69baae
643684cbf5964b1cf52b725d
643cb784ab727a49d61ca61e
643cb9bfacd2465c4462d28a
643cbf5b91028961b835b3d1
643cc36536e9385380715cfb
643cc8fadd46de1f48800b6c
643cca87249b8c0c6a4ff113
643d01977e533324c733f9c5
643d02b73b12b515be7fb69c
643d02c2f53c845e775d9ff5
643d034184dc3b561d703c7e
643d045cc7b70c2c1445a830
643cc3dc5b72c117c019651a
643d0ab34a293b21455dae93"""
list_take = list_take.split('\n')
school = info.Domain('bvl','bvl')
for take in list_take:
    contest.mark_take(school,take)
