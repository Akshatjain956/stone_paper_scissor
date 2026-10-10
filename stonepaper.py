# import random
# cscore = 0
# hscore = 0

# while True:
#     print(f"Current score you-{hscore},computer-{cscore}")
#     user=int(input("1 for stone, 2 for paper , 3 for scissors"))

#     com=random.randint(1,3)
#     if user==1 and com==3:
#         hscore+=1
#         print("You won the Round")
#     elif user==2 and com==1:
#         hscore+=1
#         print("You won the Round")
#     elif user==3 and com==2:
#         hscore+=1
#         print("You won the Round")
#     elif user==com:
#         print("It was a Draw")
#     else:
#         cscore+=1
#         print("Computer won")
#     if hscore == 5:
#         print("You won the Game")
#         break
#     elif cscore==5:
#         print("Computer won the Game")
#         break    
import streamlit as st
import random

# Page settings
st.set_page_config(
    page_title="Stone Paper Scissors",
    page_icon="🪨",
    layout="centered"
)

# Initialize scores
if "cscore" not in st.session_state:
    st.session_state.cscore = 0

if "hscore" not in st.session_state:
    st.session_state.hscore = 0

if "result" not in st.session_state:
    st.session_state.result = "Choose your move!"

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""


# Game function
def play(user):
    com = random.randint(1, 3)

    choices = {
        1: "🪨 Stone",
        2: "📄 Paper",
        3: "✂️ Scissors"
    }

    st.session_state.user_choice = choices[user]
    st.session_state.computer_choice = choices[com]

    # Winner calculation
    if user == 1 and com == 3:
        st.session_state.hscore += 1
        st.session_state.result = "🎉 You won the round!"

    elif user == 2 and com == 1:
        st.session_state.hscore += 1
        st.session_state.result = "🎉 You won the round!"

    elif user == 3 and com == 2:
        st.session_state.hscore += 1
        st.session_state.result = "🎉 You won the round!"

    elif user == com:
        st.session_state.result = "🤝 It was a draw!"

    else:
        st.session_state.cscore += 1
        st.session_state.result = "💻 Computer won the round!"


# Title
st.title("🪨 📄 ✂️ Stone Paper Scissors")

st.write("### First player to reach 5 points wins!")

# Score
col1, col2 = st.columns(2)

with col1:
    st.metric("🧑 You", st.session_state.hscore)

with col2:
    st.metric("💻 Computer", st.session_state.cscore)


st.divider()

# Display choices
col1, col2 = st.columns(2)

with col1:
    st.write("### Your Choice")
    st.info(st.session_state.user_choice or "Waiting...")

with col2:
    st.write("### Computer Choice")
    st.info(st.session_state.computer_choice or "Waiting...")


# Result
st.subheader(st.session_state.result)

st.divider()

# Buttons
st.write("### Choose your move")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Stone", use_container_width=True):
        if st.session_state.hscore < 5 and st.session_state.cscore < 5:
            play(1)
            st.rerun()

with col2:
    if st.button("📄 Paper", use_container_width=True):
        if st.session_state.hscore < 5 and st.session_state.cscore < 5:
            play(2)
            st.rerun()

with col3:
    if st.button("✂️ Scissors", use_container_width=True):
        if st.session_state.hscore < 5 and st.session_state.cscore < 5:
            play(3)
            st.rerun()


# Game over
if st.session_state.hscore == 5:
    st.success("🏆 YOU WON THE GAME!")

elif st.session_state.cscore == 5:
    st.error("💻 COMPUTER WON THE GAME!")


# Restart
if st.button("🔄 Restart Game", use_container_width=True):
    st.session_state.cscore = 0
    st.session_state.hscore = 0
    st.session_state.result = "Choose your move!"
    st.session_state.user_choice = ""
    st.session_state.computer_choice = ""
    st.rerun()
