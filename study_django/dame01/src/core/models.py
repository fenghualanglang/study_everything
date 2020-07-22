import requests
class tt(object):

    def __init__(self):

        self.header = {

        # 'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding':'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '1640',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=856A22314083D7228F34116D22C631BC; _CSRFCOOKIE=282E96FBA16D6D813BAC1D6541007BCD13CEB4F0; EPTOKEN=282E96FBA16D6D813BAC1D6541007BCD13CEB4F0',
        'CSRFCOOKIE': '282E96FBA16D6D813BAC1D6541007BCD13CEB4F0',
        'Host':'ggzyjy.jiangxi.gov.cn',
        'Origin': 'http://ggzyjy.jiangxi.gov.cn',
        'Referer': 'http://ggzyjy.jiangxi.gov.cn/hygs/huiyuaninfo/pages/htgs/HeTongGongShi_Detail?rowguid=9390ed8b-8cb5-46a5-a7ae-c4ce819a9ed8',
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        # 'X-Requested-With': 'XMLHttpRequest',
                }

    def getye(self):
        url = 'http://ggzyjy.jiangxi.gov.cn/hygs/huiyuaninfo/pages/htgs/jxpHtgsDetailAction.action?cmd=page_Load&rowguid=1b54275e-d2c7-43f3-adad-29c7910257b4&isCommondto=true'
        data = {'commonDto': [{"id":"jianshedw","bind":"dataBean.jianshedw","type":"outputtext"},{"id":"zbdanweiname","bind":"dataBean.zbdanweiname","type":"outputtext"},{"id":"htno","bind":"dataBean.htno","type":"outputtext"},{"id":"htjine","bind":"dataBean.htjine","type":"outputtext"},{"id":"supplierbankname","bind":"dataBean.supplierbankname","type":"outputtext"},{"id":"supplierbankaccount","bind":"dataBean.supplierbankaccount","type":"outputtext"},{"id":"datagrid","type":"datagrid","action":"zbdwSingleModel","idField":"rowguid","pageIndex":0,"pageSize":10,"sortField":"","sortOrder":"","columns":[{"fieldName":"itemno"},{"fieldName":"itemname"},{"fieldName":"totalprice"}],"url":"jxpHtgsDetailAction.action?cmd=zbdwSingleModel","data":[]},{"id":"datagrid2","type":"datagrid","action":"defaultModel","idField":"rowguid","pageIndex":0,"pageSize":30,"sortField":"","sortOrder":"","columns":[{"fieldName":"attachfilename"}],"url":"jxpHtgsDetailAction.action?cmd=defaultModel","data":[]},{"id":"_common_hidden_viewdata","type":"hidden","value":""}]}
        res = requests.post(url, params=data, headers=self.header)
        tt = res.content
        return tt


    def run(self):
        tt = self.getye()
        print(tt)
if __name__ == '__main__':
    t = tt()
    t.run()