import os

api_id = int(os.environ.get("API_ID", "26662728"))
api_hash = os.environ.get("API_HASH", "562302fa6d2e82bf399880f3b1250cf8")
bot_token = os.environ.get("BOT_TOKEN", "5835706516:AAETpXkhqCVc1isTRRHc83r8fe9nbXVcffo")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://p:Pendii11@cluster0.m8kujry.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001277245439"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001511422552"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001307462253"))
# =========================================================== #

#Port
PORT = os.environ.get("PORT", "8080")

# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1983980399"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#AlterGirl #AlterBoy #AlterAsk #AlterFind #AlterSpill #AlterStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/a6a2175f88089079b77ce.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/932c903b1dcfb8f9780e6.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#AlterBoy / #AlterGirl untuk Mencari Pasangan, Teman , Partner dll
#AlterAsk untuk Bertanya
#AlterStory untuk Berbagi Cerita
#AlterSpill untuk Spill Masalah
#AlterFind untuk Mencari Pasangan, Teman, Partner dll
""")
