/*
 * @author: wes
 * @date: 2017-7-25
 * @desc: app.js
*/
App({
  get: function () {
    var that = this
    //调用登录接口
    wx.login({
      success: function (res) {
        var re = res
        // 用户信息
        wx.getUserInfo({
          success: function (res) {
            that.globalData.userInfo = res.userInfo
            // 登录
            wx.request({
              method: 'post',
              url: 'https://wx.jihui88.net/rest/api/shop/member/wxapplogin',
              data: {
                code: re.code,
                appid: that.globalData.appid,
                enterpriseId: that.globalData.enterpriseId,
                nickname: that.globalData.userInfo.nickName,
                skey: wx.getStorageSync('skey') || ''
              },
              header: {
                'content-type': 'application/x-www-form-urlencoded'
              },
              success: function (res) {
                if (res.data.attributes == null || res.data === '') {
                  wx.showModal({
                    title: '登录失败'
                  })
                } else {
                  that.globalData.member = res.data.attributes.data
                  wx.setStorage({
                    key: 'skey',
                    data: res.data.attributes.data.skey || ''
                  })
                }
              }
            })
          }
        })
      }
    });
  },
  getUserInfo: function () {
    if (!this.globalData.userInfo || !this.globalData.member) {
      this.get()
    }
  },
  onLaunch: function () {
     // 总网站的参数
     var that = this
     wx.getExtConfig({
       success: function (res) {
         that.globalData.appid = res.extConfig.appid,
         that.globalData.enterpriseId = res.extConfig.enterprise_id,
         that.globalData.userId = res.extConfig.user_id,
         that.globalData.primaryColor = res.extConfig.primaryColor
         console.log('appid---' + res.extConfig.appid)
         console.log('entid---' + res.extConfig.enterprise_id)
         // 登录用户信息
         that.getUserInfo()
       }
     })
   },

  onShow: function () {
    console.log('App Show')
  },
  onHide: function () {
    console.log('App Hide')
  },
  // 全局变量
  globalData: {
    userInfo: null,
    member: null,
    accentColor: '#c00'
  }
})
