import { Component } from '@angular/core';
import { Products, products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  allproducts: Products[] = products;
  filtered_products = [...products];
  selectedCategory : string = "None";
  

  share() {
    window.alert('The product has been shared!');
  }


  filterByCategory() {
    if(this.selectedCategory == 'None') {
      this.filtered_products = this.allproducts
    } else {
      this.filtered_products = this.allproducts.filter(product => product.category === this.selectedCategory);
    }
  }

  updateFilteredProducts(value: string){
    this.selectedCategory = value;
    console.log(this.selectedCategory)
    this.filterByCategory();
  }

  incrementLikes(id : number) {
    products.filter(product => product.id === id).map(product => product.like += 1)
  }


  deleteProduct(id : number) {
    this.allproducts = this.allproducts.filter(product => product.id !== id);
    this.filterByCategory();
  }
}



