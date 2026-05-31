product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True:
    choice = (input("""===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
                    lựa chon của bạn: 
                    """).strip())
    if  choice not in ("1", "2", "3", "4", "5"):
        print ("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    if choice == "1":
        print("Danh sách sản phẩm hiện tại:")
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            for index , product in enumerate(product_list, start=1):
                if product["quantity"] == 0:
                    status = ("Hết hàng")
                elif product["quantity"] <= 5:
                    status = ("Sắp hết hàng.")
                else:
                    status = ("Còn hàng.")

                print(f"{index}. "
                      f"Mã SP: {product['product_id']} |"
                      f"Tên: {product['product_name']} |"
                      f"Giá: {product['price']} |"
                      f"Tồn kho: {product['quantity']} |"
                      f"Trạng thái: {status}")
    elif choice == "2":
        new_id = input("Nhập mã sản phẩm mới: ").strip().upper()
        is_duplicate = False
        for product in product_list:
            if product["product_id"] == new_id:
                is_duplicate = True
                break
        if is_duplicate:
            print("Mã sản phẩm đã tồn tại, vui lòng nhập mã khác.")
            continue
        new_name = input("Nhập tên sản phẩm mới: ").strip()
        new_price = input("Nhập giá sản phẩm mới: ").strip()
        new_quantity = input("Nhập số lượng sản phẩm mới: ").strip()
        if new_price.isdigit() or int(new_price) < 0:
            print("Giá sản phẩm không hợp lệ, vui lòng nhập lại.")
            continue
        if new_quantity.isdigit() or int(new_quantity) < 0:
            print("Số lượng sản phẩm không hợp lệ, vui lòng nhập lại.")
            continue
        new_product = {
            "product_id": new_id,
            "product_name": new_name,
            "price": int(new_price),
            "quantity": int(new_quantity)
        }
        product_list.append(new_product)
        print("Sản phẩm mới đã được thêm vào danh sách.")
        if choice == "3":
            update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            product_to_update = None
            for product in product_list:
                if product["product_id"] == update_id:
                    product_to_update = product
                    break
            if product_to_update is None:
                print("Không tìm thấy mã sản phẩm.")
                continue
            new_name = input("Nhập tên sản phẩm mới : ").strip()
            new_price = input("Nhập giá sản phẩm mới: ").strip()
            new_quantity = input("Nhập số lượng sản phẩm mới: ").strip()
            if new_price.isdigit() or int(new_price) < 0:
                print("Giá sản phẩm không hợp lệ, vui lòng nhập lại.")
                continue
            if new_quantity.isdigit() or int(new_quantity) < 0:
                print("Số lượng sản phẩm không hợp lệ, vui lòng nhập lại.")
                continue
            product_to_update["product_name"] = new_name
            product_to_update["price"] = int(new_price) 
            product_to_update["quantity"] = int(new_quantity)
            print("Thông tin sản phẩm đã được cập nhật.")
        elif choice == "4":
            delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            product_to_delete = None
            for product in product_list:
                if product["product_id"] == delete_id:
                    product_to_delete = product
                    break
            if product_to_delete is None:
                print("Không tìm thấy mã sản phẩm.")
                continue
            product_list.remove(product_to_delete)
            print("Sản phẩm đã được xóa khỏi danh sách.")
        elif choice == "5":
            print("Thoát chương trình.")
            break
        