import pandas as pd

# baca semua file CSV
data_a = pd.read_csv('branch_a.csv')
data_b = pd.read_csv('branch_b.csv')
data_c = pd.read_csv('branch_c.csv')

# gabungkan semua dataframe
all_data = pd.concat([data_a, data_b, data_c], ignore_index=True)

# hapus baris yang memiliki nilai NaN di kolom 'transaction_id', 'date', dan 'customer_id'
clean_data = all_data.dropna(subset=['transaction_id', 'date', 'customer_id'])

# ganti kolom 'transaction_id' ke int
clean_data['transaction_id'] = clean_data['transaction_id'].astype(int)

# ganti format kolom 'date' menjadi datetime
clean_data['date'] = pd.to_datetime(clean_data['date'])

# hilangkan duplikat berdasarkan transaction_id, ambil baris dengan tanggal terbaru
clean_data = clean_data.sort_values('date').drop_duplicates(subset='transaction_id', keep='last')

# hitung total penjualan per baris (quantity * price)
clean_data['total'] = clean_data['quantity'] * clean_data['price']

# hitung total penjualan per cabang
total_sales_per_branch = clean_data.groupby('branch')['total'].sum().reset_index()

# simpan ke file CSV
total_sales_per_branch.to_csv('total_sales_per_branch.csv', index=False)