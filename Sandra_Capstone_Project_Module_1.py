# Daftar kendaraan
rent = [
    {
        "ID": 1,
        "Size": "Small",
        "Brand": "Honda",
        "Model": "BRV",
        "Seater": 5,
        "Plate": "D 124 SML",
        "Transmission": "Manual",
        "Status": "Maintenance",
        "Tarif": 250000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 2,
        "Size": "Small",
        "Brand": "Volkswagen",
        "Model": "Polo",
        "Seater": 5,
        "Plate": "D 125 SML",
        "Transmission": "Automatic",
        "Status": "Maintenance",
        "Tarif": 240000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 3,
        "Size": "Medium",
        "Brand": "Mazda",
        "Model": "CX 3",
        "Seater": 5,
        "Plate": "D 123 MDM",
        "Transmission": "Automatic",
        "Status": "Available",
        "Tarif": 320000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 4,
        "Size": "Medium",
        "Brand": "Toyota",
        "Model": "Corolla Cross",
        "Seater": 5,
        "Plate": "D 124 MDM",
        "Transmission": "Manual",
        "Status": "Available",
        "Tarif": 300000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 5,
        "Size": "Large",
        "Brand": "Toyota",
        "Model": "Innova",
        "Seater": 7,
        "Plate": "D 123 LRG",
        "Transmission": "Automatic",
        "Status": "Rented",
        "Tarif": 400000,
        "Customer": "Budi",
        "Phone": "08234567898"
    },
    {
        "ID": 6,
        "Size": "Large",
        "Brand": "Hyundai",
        "Model": "Stargazer",
        "Seater": 7,
        "Plate": "D 124 LRG",
        "Transmission": "Manual",
        "Status": "Available",
        "Tarif": 420000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 7,
        "Size": "Premium",
        "Brand": "BMW",
        "Model": "BMW X1",
        "Seater": 5,
        "Plate": "D 123 PRM",
        "Transmission": "Automatic",
        "Status": "Available",
        "Tarif": 500000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 8,
        "Size": "Premium",
        "Brand": "Mercedes",
        "Model": "CLA 200",
        "Seater": 5,
        "Plate": "D 124 PRM",
        "Transmission": "Manual",
        "Status": "Rented",
        "Tarif": 520000,
        "Customer": "Citra",
        "Phone": "08123456789"
    },
    {
        "ID": 9,
        "Size": "Minibus",
        "Brand": "Suzuki",
        "Model": "APV",
        "Seater": 8,
        "Plate": "D 123 MNB",
        "Transmission": "Automatic",
        "Status": "Available",
        "Tarif": 600000,
        "Customer": "",
        "Phone": ""
    },
    {
        "ID": 10,
        "Size": "Minibus",
        "Brand": "Daihatsu",
        "Model": "Gran Max",
        "Seater": 5,
        "Plate": "D 124 MNB",
        "Transmission": "Manual",
        "Status": "Available",
        "Tarif": 620000,
        "Customer": "",
        "Phone": ""
    }
]

# Fungsi untuk mencetak data dalam bentuk tabel
def print_table(data):
    # Cetak header tabel
    print("{:<3} {:<10} {:<10} {:<15} {:<6} {:<15} {:<13} {:<15} {:<8} {:<10} {:<15}".format(
        'ID', 'Size', 'Brand', 'Model', 'Seater', 'Plate', 'Transmission', 'Status', 'Tarif', 'Customer', 'Phone'
    ))
    # Cetak setiap baris data
    for car in data:
        print("{:<3} {:<10} {:<10} {:<15} {:<6} {:<15} {:<13} {:<15} {:<8} {:<10} {:<15}".format(
            car["ID"], car["Size"], car["Brand"], car["Model"],
            car["Seater"], car["Plate"], car["Transmission"],
            car["Status"], car["Tarif"], car["Customer"], car["Phone"]
        ))
    print()

# Fungsi untuk menampilkan menu utama
def main_menu(rent):
    while True:
        print("--- Sandra Purwadhika Car Rental Program ---")
        print("=== Main Menu ===")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Change Data (Update / Delete)")
        print("4. Finish")

        choice = input("Choose Menu: ")

        # Pilihan menu utama
        if choice == '1':
            view_rental_data_menu()
        elif choice == '2':
            add_rental_data()
        elif choice == '3':
            change_rental_data(rent)
        elif choice == '4':
            print("Thank you, have a good day.\n\n")
            break
        else:
            print("Data does not exist, please input again")
        print()

# Fungsi untuk menampilkan menu read data
def view_rental_data_menu():
    while True:
        print("\n--- Read Data Menu ---")
        print("1. Search Data")
        print("2. All Data")
        print("3. Finish")

        choice = input("Choose Menu: ")

        # Pilihan menu lihat data
        if choice == '1':
            search_data_menu()
        elif choice == '2':
            all_data_menu()
        elif choice == '3':
            return
        else:
            print("Data does not exist, please input again")
        print()

# Fungsi untuk menampilkan menu pencarian data
def search_data_menu():
    while True:
        print("\n--- Search Data Menu ---")
        print("1. Status")
        print("2. Transmission")
        print("3. Finish")

        choice = input("Choose Menu: ")

        # Pilihan untuk mencari data berdasarkan status atau transmission
        if choice == '1':
            status = input("Status (Available / Maintenance / Rented): ").capitalize()
            filtered_data = []
            for car in rent:
                if car['Status'].capitalize() == status:
                    filtered_data.append(car)
            if filtered_data:
                print_table(filtered_data)
            else:
                print("Data does not exist, please input again")
            print()
        elif choice == '2':
            transmission = input("Choose Manual / Automatic: ").capitalize()
            filtered_data = []
            for car in rent:
                if car['Transmission'].capitalize() == transmission:
                    filtered_data.append(car)
            if filtered_data:
                print_table(filtered_data)
            else:
                print("Data does not exist, please input again")
            print()
        elif choice == '3':
            return
        else:
            print("Data does not exist, please input again")
        print()

# Fungsi untuk menampilkan semua data dan mengurutkannya
def all_data_menu():
    print("\n--- View Sort from All Data Menu ---")
    print("1. Sort by ID")
    print("2. Sort by Tarif")
    print("3. Finish")

    choice = input("Choose Menu: ")

    # Pilihan untuk mengurutkan data berdasarkan ID atau Tarif
    if choice == '1':
        sorted_data = sorted(rent, key=lambda x: x["ID"])
        print_table(sorted_data)
    elif choice == '2':
        sorted_data = sorted(rent, key=lambda x: x["Tarif"], reverse=True)
        print_table(sorted_data)
    elif choice == '3':
        return
    else:
        print("Data does not exist, please input again")
    print()

# Fungsi untuk menambahkan data rental baru
def add_rental_data():
    print_table(rent)
    new_id = int(input('Input "ID": '))
    size = input('Input "Size": ')
    brand = input('Input "Brand": ')
    model = input('Input "Model": ')
    seater = int(input('Input "Seater": '))
    plate = input('Input "Plate": ')
    transmission = input('Input "Transmission": ')
    status = input('Input "Status": ')
    tarif = int(input('Input "Tarif": '))
    customer = input('Input "Customer": ')
    phone = input('Input "Phone": ')

    # Tambahkan data baru ke dalam daftar rent
    rent.append({
        "ID": new_id,
        "Size": size,
        "Brand": brand,
        "Model": model,
        "Seater": seater,
        "Plate": plate,
        "Transmission": transmission,
        "Status": status,
        "Tarif": tarif,
        "Customer": customer,
        "Phone": phone
    })

    print("\nNew data successfully added.\n")
    print_table(rent)
    print()
    return

# Fungsi untuk mengubah atau menghapus data rental yang ada
def change_rental_data(rent):
  while True:
    print_table(rent)
    print("\n--- Change Data Menu ---")
    print("1. Update Data")
    print("2. Delete Data")
    print("3. Finish")

# Masuk ke pilihan menu untuk update/delete data
    choice = input("Choose Menu: ")

    if choice == '1':
      # Memberi input untuk id mobil yang akan diganti/didelete
      id_car = int(input("Input Car ID: "))
      car_found = False
      for item in rent:
        if item["ID"] == id_car:
            car = item
            car_found = True
            break
      if not car_found:
        print("Data does not exist, please input again")
        continue
      while True:
          print("Edit Field:")
          print("1. Tarif")
          print("2. Status")
          print("3. Finish")

          choice = input("Choose Menu: ")

          # Pilihan untuk mengubah tarif atau status kendaraan
          if choice == '1':
              new_tarif = int(input("New Tarif: "))
              car["Tarif"] = new_tarif
              print("Data successfully updated.")
              print_table(rent)

          elif choice == '2':
              new_status = input("New Status (Available / Maintenance / Rented): ").capitalize()
              car["Status"] = new_status
              if new_status == "Rented":
                  car["Customer"] = input("Customer: ")
                  car["Phone"] = input("Phone: ")
              else:
                  car["Customer"] = ""
                  car["Phone"] = ""
              print("Data successfully updated.")
              print_table(rent)
          elif choice == '3':
              break
          continue
# Jika ingin delete data
    elif choice == '2':
      # Memberi input untuk id mobil yang akan diganti/didelete
      id_car = int(input("Input Car ID: "))
      car_found = False
      for item in rent:
        if item["ID"] == id_car:
            car = item
            car_found = True
            break
      if not car_found:
        print("Data does not exist, please input again")
        continue
      while True:
        if car in rent:
          rent.remove(car)
          print_table(rent)
          print(f'Car data with car ID {id_car} is successfully deleted.')
        else:
          print(f'Car data with car ID {id_car} is not found.')
          break
        continue
    elif choice == '3':
      break


def login():
    while True:  # Loop to allow re-login after exiting the main menu
        print("\t\tADMIN PAGE")
        print("\n\t=========================")
        print ("\t\t\t\tby Sandra")
        print("\n")
        count = 0 
        while count < 3:
            print("To exit please write (exit)")
            login = input("Enter your password: ")
            if login == "exit":
                return  
            if login == "Jakarta":
                main_menu(rent)
                break  
            else:
                print("Please re-enter your password")
                count += 1
        else:
            print("Please contact your manager")
            return  

login()
