import logging #1、导入模块logging

def log():
    logger=logging.getLogger() #2、创建（获得）日志对象（只创建一次对象）
    if not logger.handlers: #如果logger对象中不存在处理器
        logger.setLevel(logging.INFO) #3、设置日志（最低输出）等级
        formater=logging.Formatter('%(asctime)s %(levelname)s [%(message)s] %(filename)s:%(lineno)s') #4、设置日志输出格式
        console=logging.StreamHandler() #5、创建日志流处理器（输出到控制台）
        console.setFormatter(formater) #6、设置日志流处理器的输出格式
        logger.addHandler(console) #7、日志流处理器增加到日志对象
        console.close() #8、关闭日志流处理器（日志对象负责输出日志）
        file=logging.FileHandler('../log/exam.log', encoding='utf-8') #9、创建日志文件处理器，可省参数mode表示写入模式，默认是追加
        file.setFormatter(formater) #10、设置日志文件处理器的输出格式
        logger.addHandler(file) #11、日志文件处理器增加到日志对象
        file.close() #12、关闭日志文件处理器
    return logger
#调试：输出日志
if __name__=='__main__':
    log().info('成功的消息')
    log().warning('警告信息')
    log().error('错误信息')