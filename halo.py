import streamlit as st

topping_price = 5,5,6,7,8,10  
topping_list = 'Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)',  'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'


st.title("Trà Sữa COTAI")
size = st.radio("Kích cỡ",('Nhỏ (30K)', 'Vừa (40K)', 'Lớn (50K)'), horizontal=True)
st.text("Thêm")
col1,col2,col3,col4 = st.columns(4)
with col1:
  milk = st.checkbox("Sữa (5K)")
with col2:
  cafe = st.checkbox("Cà phê (8K)")
with col3:
  cream = st.checkbox("Kem (10K)")
with col4:
  egg = st.checkbox("Trứng (15K)")
topping = st.multiselect('Topping', topping_list)
n = st.number_input('Số lượng', min_value=1, step=1)
text = st.text_input('Ghi chú')
if st.button('Đặt'):
  st.write("Cỡ ", size)
  st.write("Thêm:", milk, cream , cafe, egg)
  st.write("Topping: ", topping)
  st.write(text)
  st.write("Số lượng:",n)
  if size == 'Nhỏ (30K)':
    price = 30
  elif size =='Vừa (40K)':
    price = 40
  else:
    price = 50
  money = n * (price + milk*5 + cafe*8 + cream*10 + egg*15 + topping_money)
  st.success('Thành tiền: ' + str(money) + 'K')
