# coding: utf-8
import argparse
import datetime
import os
import time


def today():
    return time.strftime("%Y-%m-%d")


def file_update(path):
    try:
        return int(os.path.getmtime(path))
    except:
        # 文件不存在，返回0点时间戳
        print("{} file not exists".format(path))
        return int(time.mktime(datetime.date.today().timetuple()))


def timestamp():
    return int(time.time())


def file_check_update(path, check_time):
    path = path.format(date=today())
    last_time = file_update(path)
    print("{} last_time {}".format(path, last_time))
    # 超过确认时间未发生更新
    if timestamp() - last_time > check_time:
        return False
    else:
        return True


def output(status, name="wx-notice"):
    with open(name, 'w') as file:
        file.write(str(status))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # yapf: disable
    parser.add_argument('-p', '--path', type=str,
                        default=4000, help='listen port')
    parser.add_argument('-t', '--time', type=int, default=300)
    args = parser.parse_args()

    if not file_check_update(args.path, args.time):
        print("file check update abnormal")
        output(0)
    else:
        output(1)


if __name__ == '__main__':
    main()
