import datetime as dt
from schedule.models import Task

class Controller():

    def get_time_length(self, single_task):
        print("single_task",single_task)
        start = dt.datetime.strptime(single_task[0], "%Y-%m-%d %H:%M:%S")
        end = dt.datetime.strptime(single_task[1], "%Y-%m-%d %H:%M:%S")

        time_length = (end - start).total_seconds() / 60

        return time_length

    def is_task_insert_able(self, task_data, insert_data):
        start_time = insert_data[0]
        end_time = insert_data[1]

        schedule_data = task_data[2:]

        for task in schedule_data:
            reserved_start_time = task[0]
            reserved_end_time = task[1]
            print(start_time, end_time, reserved_start_time, reserved_end_time)
            # 넣는 시작시간 보다 종료시간이 늦으면 겹침
            if reserved_start_time < start_time:
                if start_time < reserved_end_time:
                    return False

            # 넣는 종료 시간보다 시작시간이 이르면  겹침
            else:
                if end_time > reserved_start_time:
                    return False

        return True

    def insert(self, username, user_data, insert_data):

        if user_data == []:
            username = "hyunho"
            user_data.append(username)
            user_data.append(0)
            user_data.append(insert_data)
            return [user_data]

        # TODO 삽입될 때 마다 길이를 잰다
        # TODO RULE1 가장 긴 녀석 부터 가장 아래에 배치한다.
        # TODO RULE2 줄에 들어갈 수 있는지 검사해야한다.

        task_bag = []
        task_bag.append((insert_data, self.get_time_length(insert_data)))

        for line in user_data:
            items = line[2:]
            for item in items:
                task_bag.append((item, self.get_time_length(item)))

        task_bag = self.sort_task(task_bag)

        print("task_bag", task_bag)
        print("==================")

        username = "hyunho"
        temp_user_data = []
        temp_line_data = []
        line_num = 0
        for item in task_bag:
            print("item", item)
            # 첫번째 삽입
            if temp_user_data == []:
                temp_line_data.append(username)
                temp_line_data.append(line_num)
                temp_line_data.append(item[0])
                temp_user_data.append(temp_line_data)
            else:
                for line_num in range(0, 7):
                    # 줄을 생성할 필요가 없다
                    print("line_info", temp_user_data, len(temp_user_data), line_num)
                    if len(temp_user_data) > line_num:
                        temp_line_data = temp_user_data[line_num]
                        # 현재 줄에 삽입할 수 있으면 삽입한다.
                        if self.is_task_insert_able(temp_line_data, item[0]):
                            temp_line_data.append(item[0])
                            break
                        else:
                            temp_line_data = []
                            print("이번줄에 삽입불가")
                        # 불가능 하면 다음 줄에 삽입한다.
                    # 줄을 생성헤서 데이터를 넣어야 한다.
                    else:
                        temp_line_data.append(username)
                        temp_line_data.append(line_num)
                        temp_line_data.append(item[0])
                        temp_user_data.append(temp_line_data)
                        print("들어갔디")
                        break
                    print("한바퀴")
            print("temp_user_data", temp_user_data)
            print("===================")
        return temp_user_data

    def update(self, user_data, origin_task, update_task):
        username = "hyunho"

        user_data = self.remove_task(user_data, origin_task)

        user_data = self.insert(username, user_data, update_task)

        return user_data

    def remove_task(self, user_data, remove_target_task):
        for line in user_data:
            for task in line:
                if remove_target_task == task:
                    line.remove(task)

        return user_data

    def sort_task(self, tasks):
        tasks.sort(key=lambda element: element[1], reverse=True)
        return tasks


    def insert_to_db(self,task):
        username = "hyunho"
        start_time = task[0]
        end_time = task[1]
        t = Task(username=username,task_start=start_time,task_end=end_time,is_deleted=0)
        t.save()


"""

   def select(self):
        '''
        temporary data
        '''
        username = "hyunho"
        return user_data
        
    def sort_task(self,task_data):
        tasks = []
        for task in task_data:
            
        return task_data


    # TODO : AFTER CONNECT DATABASE
    
    def select(self, username):

        return user_data
        
        
    def delete(self):
        return True
    
"""
