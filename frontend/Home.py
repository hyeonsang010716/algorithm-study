from util.crawling import get_data
import streamlit as st
import requests
import os
import asyncio

st.set_page_config(page_title="알고리즘 프로젝트", page_icon="💬")

class Basic:

    def __init__(self):

        self.server_url = "http://localhost:8001"

        if "name" not in st.session_state:
            st.session_state["name"] = None

        if "session_disable" not in st.session_state:
            st.session_state["session_disable"] = True

        if "session_id_input_disable" not in st.session_state:
            st.session_state["session_id_input_disable"] = False
        
        if "problem_numbers" not in st.session_state:
            st.session_state["problem_numbers"] = None

    def session_enable(self):
        st.session_state["session_disable"] = False
        st.session_state["session_id_input_disable"] = True
        return

    def session_disable(self):
        st.session_state["session_disable"] = True
        st.session_state["session_id_input_disable"] = False
        return

    def send_problem_number_to_server(self):
        """ 서버에 문제 번호를 요청합니다."""
        
        name = st.session_state["name"]
        
        response = requests.post(f"{self.server_url}/{name}/chat/problem_number")
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error communicating with the server.")
            return None


    def send_problem_input_to_server(self, user_query):
        """서버에 요청을 보내고 응답을 받습니다."""

        name = st.session_state["name"]

        data = {"input": user_query}

        response = requests.post(f"{self.server_url}/{name}/chat/algorithm", json=data)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error communicating with the server.")
            return None
        
    async def main(self):

        st.sidebar.divider()

        st.session_state["name"] = st.sidebar.selectbox("이름 선택", ["hyeonsang" , "UH" , "dbwognl" , "sentryc"] , disabled=st.session_state["session_id_input_disable"])

        if st.session_state["name"]: 
            session_start = st.sidebar.button(
                "세션 시작",
                disabled=st.session_state["session_id_input_disable"],
                on_click=self.session_enable,
            )

            if session_start:
                name = st.session_state["name"]
                st.sidebar.info(f"{name}님 세션을 시작합니다.")

        else: 
            st.sidebar.warning("이름을 선택해주세요.")


        if st.session_state["name"] != "dbwognl":

            if st.button("문제 요청" , disabled=st.session_state["session_disable"]):
                st.session_state["problem_numbers"] = self.send_problem_number_to_server()["answer"]
                
        else:
            
            st.session_state["problem_numbers"] = st.chat_input(
                placeholder="문제 번호를 입력하세요.",
                disabled=st.session_state["session_disable"],
            )


        if st.session_state["problem_numbers"]:

            stat , content , inputs , outputs = get_data(st.session_state["problem_numbers"])

            try:
                if stat:
                    st.write(content)
                    
                    answers = self.send_problem_input_to_server(inputs)["answer"]
                    
                    ai = ""
                    
                    human = ""
                    
                    for i in range(1 , len(inputs)+1):
                        ai += f"## 예제 {i}" + "\n"
                        ai += "#### 입력" + "\n"
                        ai += inputs[i-1] + "\n"
                        ai += "#### 출력" + "\n"
                        ai += outputs[i-1] + "\n"

                        human += "#### 정답" + "\n"
                        human += answers[i-1] + "\n"

                        st.chat_message("ai").write(ai.replace("\n", "  \n"))
                        st.chat_message("human").write(human.replace("\n", "  \n"))
                        
                        ai = ""
                        human = ""
                    
                else:
                    st.write("요청 에러 문제 숫자만 입력해주세요.")
            except Exception as e:
                print(e)
                st.write("요청 에러 문제 숫자만 입력해주세요.")


if __name__ == "__main__":
    obj = Basic()
    # obj.main()
    asyncio.run(obj.main())
