import React from 'react';
import HomePage from './HomePage';
import { render, screen } from '@testing-library/react';

test ('renders HomePage', ()=>{
    render(<HomePage/>);
    const linkElement = screen.getByTestId('home-page');

    expect(linkElement).toBeInTheDocument();
});

test ('renders Animated div', ()=>{
    render(<HomePage/>);
    const linkElement = screen.getByText('My Component');

    expect(linkElement).toBeInTheDocument();
});

test ('Animation happens', ()=>{
    render(<HomePage/>);
    const linkElement = screen.getByText('Click To Animate');
    linkElement.click();

    const animatedElement = screen.getByText('My Component');
    expect(animatedElement).toHaveStyle('color: red');
});