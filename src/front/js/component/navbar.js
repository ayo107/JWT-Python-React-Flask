import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light mb-3">
			<Link to="/">
				<span className="navbar-brand mb-0 h1">
					<img
						src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRsnUXkrv5QBuWx6TYrKxNqIXa5JPdUhwLfAzN432_Dg3HyrnFEc-Y79Kl7wonvg5pP4E&usqp=CAU"
						width="60"
						height="40"
					/>
				</span>
			</Link>
			<div className="ml-auto">
				<Link to="/protected">
					<button className="btn btn-primary">User Zone</button>
				</Link>
				<Link to="/login">
					<button className="btn btn-primary">Login</button>
				</Link>
				<Link to="/signup">
					<button className="btn btn-primary">Sign Up!</button>
				</Link>
			</div>
		</nav>
	);
};