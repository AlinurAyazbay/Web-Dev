import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {
  name = '';
  email = '';
  message = '';
  submitted = false;

  submitForm() {
    if (this.name && this.email && this.message) {
      this.submitted = true;
      alert('Thank you for your message!');
      this.resetForm();
    } else {
      alert('Please fill out all fields.');
    }
  }

  resetForm() {
    this.name = '';
    this.email = '';
    this.message = '';
  }
}
