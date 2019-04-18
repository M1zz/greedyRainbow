class Controller():

    def is_insert_able(self, user_data, insert_data):
        start_time = insert_data[0]
        end_time = insert_data[0]

        schedule_data = user_data[2:]

        for task in schedule_data:
            reserved_start_time = task[0]
            reserved_end_time = task[1]

            # 넣는 시작시간 보다 종료시간이 늦으면 겹침
            if reserved_start_time < start_time:
                if start_time < reserved_end_time:
                    return False

            # 넣는 종료 시간보다 시작시간이 이르면  겹침
            else:
                if end_time > reserved_start_time:
                    return False

        return True

    def insert(self, user_data, insert_data):

        info = user_data[:2]
        if self.is_insert_able(user_data, insert_data):
            user_data.append(insert_data)
        else:
            info[1] = int(info[1]) + 1
            info.append(insert_data)
            return info

        return user_data
